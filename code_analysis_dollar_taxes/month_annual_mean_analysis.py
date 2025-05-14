#Essa é uma análise da média Mês-ano das taxas de câmbio

import matplotlib.pyplot as matplt
import matplotlib.dates as mdates
import locale

# Aqui estamos tentando configurar a localidade para português
try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')  # Linux/Mac
except:
    try:
        locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')  # Windows
    except:
        print("Não foi possível definir a localidade correta para o Português-BR, então os nomes podem aparecer em inglês")

# Vamos criar uma coluna 'MesAno' com o formato mês-ano para agregação
df_dados['MesAno'] = df_dados['Data'].dt.to_period('M')

# Calculamos a média da taxa de câmbio por mês
df_aggregated = df_dados.groupby('MesAno')['Taxa Câmbio'].mean().reset_index()

# Convertermos a coluna, eixo x, 'MesAno' para timestamp (datetime)
df_aggregated['MesAno'] = df_aggregated['MesAno'].dt.to_timestamp()

# Vamos solicitar ao usuário o ano de início para visualizar os dados
ano_inicio_filtro = int(input("Digite o ano de início para visualizar os dados (ex: 2020): "))

# Aqui vamos filtrar os dados no DF a partir do ano selecionado
df_filtrado = df_aggregated[df_aggregated['MesAno'].dt.year >= ano_inicio_filtro]

# Aqui temos as configurações para o plot do gráfico
matplt.figure(figsize=(12, 6))
matplt.plot(df_filtrado['MesAno'], df_filtrado['Taxa Câmbio'], marker='o', linestyle='-', label='Taxa de Câmbio Média')
matplt.title(f'Taxa de Câmbio Média por Mês-Ano (a partir de {ano_inicio_filtro})', fontsize=18, fontweight='bold', fontname='Arial', pad=15)

#Configurações dos eixos X e Y
matplt.xlabel('Mês-Ano', fontsize=12, fontweight='light', fontname='Arial',labelpad=15, loc = 'center')
matplt.ylabel('Taxa de Câmbio Média', fontsize=12, fontweight='light', fontname='Arial',labelpad=15, loc = 'center')

#Configuração do tamanho da fonte dos ticks
matplt.tick_params(axis='x', labelsize=10,rotation=60)
matplt.tick_params(axis='y', labelsize=10)

#Configuração do grid do gráfico
matplt.grid(True, linestyle='dotted', color='gray', alpha=0.2)

# Aqui vamos garantir que a formatação do eixo X esteja no estilo "jan-2024"

matplt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
matplt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b-%Y'))

# Ajusta o layout final
matplt.tight_layout()
matplt.legend()
matplt.show()

