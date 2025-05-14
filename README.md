# Webscraping: IPEA Data

[![Leia em Inglês](https://img.shields.io/badge/Ler%20em-Inglês-blue)](README_eng.md)

## Sobre o Projeto

Este projeto demonstra minhas habilidades em web scraping, análise de dados e visualização utilizando Python.

O principal objetivo é analisar a cotação histórica do dólar americano (USD) em relação ao real brasileiro (BRL), investigando como eventos globais importantes influenciaram suas variações ao longo dos anos. Os dados foram coletados por meio de técnicas de web scraping e processados com bibliotecas Python como BeautifulSoup (bs4), Pandas e Matplotlib.

Mais do que a execução técnica, este projeto simula o desenvolvimento de uma análise financeira replicável, que poderia ser incorporada a um relatório de inteligência de mercado para uma empresa do setor financeiro.

O objetivo é oferecer insights valiosos, ao mesmo tempo em que demonstra como o Python pode ser aplicado na análise de dados financeiros do mundo real.


## Resumo - Documentação Técnica

### 1) Requisição HTTP

Estamos lidando com um website, portanto, temos que tratar isso como uma requisição. Logo, os primeiros passos foi a busca da URL e definição da função de requisição.
Além disso, também implementei uma validação para verificar se a resposta foi bem-sucedida (status code 200).

### 2) Parsing do HTML

* Utiliza BeautifulSoup para fazer o parsing do conteúdo da página HTML.

Localização da Tabela

Tenta localizar a tabela com ID 'grd_DXMainTable' (padrão em páginas ASP.NET com DevExpress).

Se não encontrar, busca dentro de <div id="divGrid"> uma <table class="dxgvTable_Moderno"> (fallback).

Identificação do Cabeçalho

Tenta localizar os cabeçalhos com a classe 'dxgvHeader_Moderno'.

Se não encontrar, aplica uma lógica alternativa para inferir o cabeçalho a partir das primeiras linhas da tabela.

Como fallback final, define manualmente os nomes das colunas: ['Data', 'Taxa de câmbio - R$ / US$ - comercial - compra - média'].

Extração das Linhas de Dados

Procura por linhas com a classe 'dxgvDataRow_Moderno'.

Se não houver, tenta identificar linhas de dados com base na quantidade de colunas e na ausência de elementos <input> (filtros).

Garante que o número de colunas das linhas de dados seja igual ao número de colunas do cabeçalho.

Criação do DataFrame

Constrói um pandas.DataFrame com os dados extraídos e os nomes de colunas identificados.

Tratamento de Exceções

Captura e imprime erros de requisição (RequestException) ou outros erros de execução
