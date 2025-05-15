# Webscraping: IPEA Data

[![Leia em Inglês](https://img.shields.io/badge/Ler%20em-Inglês-blue)](README_eng.md)

## 💼 Sobre o Projeto

Este projeto demonstra minhas habilidades em web scraping, análise de dados e visualização utilizando Python.

O principal objetivo é analisar a cotação histórica do dólar americano (USD) em relação ao real brasileiro (BRL), investigando como eventos globais importantes influenciaram suas variações ao longo dos anos. Os dados foram coletados por meio de técnicas de web scraping e processados com bibliotecas Python como BeautifulSoup (bs4), Pandas e Matplotlib.

Mais do que a execução técnica, este projeto simula o desenvolvimento de uma análise financeira replicável, que poderia ser incorporada a um relatório de inteligência de mercado para uma empresa do setor financeiro.

O objetivo é oferecer insights valiosos, ao mesmo tempo em que demonstra como o Python pode ser aplicado na análise de dados financeiros do mundo real.


## 🔎 Onde encontrar?

### code_webscraping:
Aqui tem o código em Python com a extração dos dados do website IPEA Data. Desde o momento de extração até o tratamento dos dados e armazenamento deles em variáveis que serão usadas nas análises.

### code_analysis_dollar_taxes

Nessa pasta contém o código para as 3 análises realizadas + arquivo README.md com análise escrita[code_analysis_dollar_taxes/analise.md]em versão em inglês e português.


## 👩🏻‍💻 Resumo - Documentação Técnica

### 1) Requisição HTTP

Estamos lidando com um _website_, portanto, temos que tratar isso como uma requisição. Logo, os primeiros passos foi a busca da URL e definição da função de requisição.

Além disso, também implementamos uma validação para verificar se a resposta foi bem-sucedida (status code 200).

### 2) Parsing HTML

Para realizar o parsing, que nada mais é do que uma leitura na página, utilizamos o BeautifulSoup para fazer isso. Algo muito importante aqui é prover informações para que a tabela ou dados que necessitem ser localizados, assim sejam. 

Por conta disso, implementamos a localização padrão de tabela, considerando ID 'grd_DXMainTable' (padrão em páginas ASP.NET com DevExpress).
Aqui se essa localização não for bem sucedida, garantimos que a tabela será encontrada com uma outra busca:  class="dxgvTable_Moderno".


### 3) Identificação do Cabeçalho

Uma vez que os dados da tabela foram encontrados, agora é tentar localizar os cabeçalhos e isso fizemos usando a classe 'dxgvHeader_Moderno'.
Se não encontrar, aplica uma lógica alternativa para inferir o cabeçalho a partir das primeiras linhas da tabela.

Por se tratar de um website relativamente simples, como _fallback_ final, definimos manualmente os **nomes das colunas: ['Data', 'Taxa de câmbio - R$ / US$ - comercial - compra - média'].**

### 4) Extração das Linhas de Dados

Assim que o cabeçalho foi encontrado, vamos procurar por linhas com a classe 'dxgvDataRow_Moderno'.
Se não houver, tenta identificar linhas de dados com base na quantidade de colunas e na ausência de elementos.

Logo em seguida, foi necessário implementar uma regra que garantisse que o número de colunas das linhas de dados seja igual ao número de colunas do cabeçalho.

### 5) Criação do DataFrame

Usando pandas, construímos um _pandas.DataFrame_ com os dados extraídos e os nomes de colunas identificados. Também fizemos algumas alterações nos nomes das colunas para que fosse mais fácil trabalhar na parte da análise.

### 6) Tratamento de Exceções

Em todo o código você vai ver que lidamos com os possíveis erros por meio de exceções e prints de logs de erro.
