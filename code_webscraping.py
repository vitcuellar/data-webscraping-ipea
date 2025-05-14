#Código de implementação de método webscraping para o website IPEA Data

def extrair_dados_ipeadata(url):
    """
    Extrai os dados da tabela do site IPEADATA que contém cotação diária do dólar desde 1985.

    Argumentos de entrada:
        A URL da página que contém a tabela (string).

    Retorno ou resposta experada:
        pandas.DataFrame: Um DataFrame contendo os dados da tabela.
    
    """
    try:
        # Aqui fazemos a requisição HTTP para obter o conteúdo da página
        response = requests.get(url) 
        # Verificação se a requisição foi bem-sucedida (status code 200)
        response.raise_for_status()  

        # Implementamos o BeautifulSoup para fazer o parsing do HTML 
        soup = BeautifulSoup(response.content, 'html.parser')

        # Aqui vamos tentar encontrar a tabela com o ID 'grd_DXMainTable' que é comum em páginas ASP.NET com DevExpress.
        tabela = soup.find('table', id='grd_DXMainTable')

        if not tabela:
            # Se não encontrar pelo ID, vamos tentar uma abordagem mais genérica. A ideia aqui é procurar por tabelas que possam conter os dados.
            # Isso pode ser útil se o ID mudar ou se houver múltiplas tabelas na página. Você pode adaptar para outro projeto, se necessário.
            # Para o IPEADATA, a tabela de dados principal está dentro de <div id="divGrid"> e a tabela em si é <table class="dxgvTable_Moderno".
            div_grid = soup.find('div', id='divGrid')
            if div_grid:
                tabela = div_grid.find('table', class_='dxgvTable_Moderno')

        # Aqui uma regra para extrairmos os dados da tabela
        linhas = tabela.find_all('tr')

        # Extraímos o cabeçalho da tabela (considerando que o cabeçalho pode estar em <th> ou <td>). 
        # A primeira linha da tabela no IPEADATA pode conter filtros ou ser parte do cabeçalho.Para isso,a regra do if abaixo.
        # No if abaixo, verificamos se a classe 'dxgvHeader_Moderno' existe. Se não existir, tentamos pegar o cabeçalho de outra forma.
        
        cabecalho_tipo = tabela.find_all('td', class_='dxgvHeader_Moderno')
        if not cabecalho_tipo: # Fallback se a classe não for encontrada
             primeira_linha_cabecalho = None
             for i, linha in enumerate(linhas):
                 if len(linha.find_all('td')) > 1: # Procura a primeira linha com múltiplas colunas de dados
                     primeira_linha_cabecalho = i
                     break
             if primeira_linha_cabecalho is not None and primeira_linha_cabecalho > 0: # Assumindo que o cabeçalho está antes dos dados
                cabecalho_tipo = linhas[primeira_linha_cabecalho -1].find_all(['th', 'td'])

        # Se o cabeçalho foi encontrado, extraímos os textos
        nome_colunas_cabecalho = [th.get_text(strip=True) for th in cabecalho_tipo]

        # Se o cabeçalho não for encontrado nesse formato, podemos tentar pegar da primeira linha ou definir manualmente (escolha aplicada).
        # Para este caso, o IPEADATA tem "Data" e "Taxa de câmbio - R$ / US$ - comercial - compra - média" como nome das colunas.
        
        if not nome_colunas_cabecalho or len(nome_colunas_cabecalho) < 2 : # Verifica se o cabeçalho tem pelo menos 2 colunas esperadas
            print(f"Cabeçalho não identificado, usando {nome_colunas_cabecalho} como padrão.")
            nome_colunas_cabecalho = ['Data', 'Taxa de câmbio - R$ / US$ - comercial - compra - média']
            
        # Extrai os dados das linhas restantes e armazena em uma lista
        dados_ipea_cambio = []
        
        # As linhas de dados no IPEADATA têm a classe 'dxgvDataRow_Moderno'
        linhas_de_dados = tabela.find_all('tr', class_='dxgvDataRow_Moderno')

        if not linhas_de_dados: # Tentativa de pegar linhas de dados sem a classe específica
            # Se não encontrar linhas com a classe 'dxgvDataRow_Moderno', tentamos pegar todas as linhas
            # Isso pode ser útil se a estrutura da tabela mudar ou se houver múltiplas tabelas na página.
            
            linhas_de_dados_potenciais = []
            inicio_dados = False
            for linha in linhas:
                celulas = linha.find_all('td')
                # Consideramos uma linha de dados se tiver o número esperado de colunas (2 neste caso) e não for uma linha de cabeçalho ou filtro.
                if len(celulas) == len(nome_colunas_cabecalho):
                    # Verificando se não é uma linha de cabeçalho ou filtro
                    if not celulas[0].find('input'):
                        linhas_de_dados_potenciais.append(linha)

            if not linhas_de_dados_potenciais:
                print("Nenhuma linha de dados encontrada.")
                return None
            linhas_de_dados = linhas_de_dados_potenciais

        # Aqui temos a extração dos dados de cada linha
        for linha in linhas_de_dados:
            celulas = linha.find_all('td')
            if len(celulas) == len(nome_colunas_cabecalho): # Essa regra é para garantir que temos o mesmo número de colunas que o cabeçalho
                valores_linha = [td.get_text(strip=True) for td in celulas]
                dados_ipea_cambio.append(valores_linha)

        if not dados_ipea_cambio:
            print("Nenhum dado extraído da tabela.")
            return None

        # Por fim, aqui criamos um DataFrame do Pandas com os dados
        df = pd.DataFrame(dados_ipea_cambio, columns=nome_colunas_cabecalho)
        return df
    # Tratamento de exceções para erros de requisição ou parsing
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro durante o scraping: {e}")
        return None

# URL fornecida
url_ipeadata = "http://www.ipeadata.gov.br/ExibeSerie.aspx?serid=38590&module=M"

# Chamando a função para extrair os dados
df_dados = extrair_dados_ipeadata(url_ipeadata)


