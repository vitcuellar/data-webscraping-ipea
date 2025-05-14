#Essa é uma análise da média anual da taxa de câmbio 

import matplotlib.pyplot as matplt

# Criar uma coluna 'Ano' para agregação
df_dados['Ano'] = df_dados['Data'].dt.to_period('Y')

# Calcular a média da Taxa de Câmbio agrupada por ano
df_annual = df_dados.groupby('Ano')['Taxa Câmbio'].mean().reset_index()

# Converter 'Ano' para datetime para facilitar a plotagem
df_annual['Ano'] = df_annual['Ano'].dt.to_timestamp()

# Criar o gráfico
matplt.figure(figsize=(13, 7))

# Solicitar ao usuário o ano de início
ano_inicio_filtro = int(input("Digite o ano de início para visualizar os dados (ex: 2020): "))

# Filtrar os dados a partir do ano escolhido pelo usuário
df_filtrado_ano = df_annual[df_annual['Ano'].dt.year >= ano_inicio_filtro]

# Plotar a média anual da taxa de câmbio
matplt.plot(df_filtrado_ano['Ano'], df_filtrado_ano['Taxa Câmbio'], marker='o', linestyle='-', label='Média Anual')

# Adicionar os valores médios no gráfico
for i, row in df_filtrado_ano.iterrows():
    matplt.text(row['Ano'],row['Taxa Câmbio'] + 0.01, f"{row['Taxa Câmbio']:.2f}", fontsize=9, ha='center', va='bottom', fontname='Arial', fontweight='black')

#Configurações do grid 
matplt.grid(True, linestyle='dotted', color='gray', alpha=0.2)


# Configurações do gráfico
matplt.title(f'Média Anual da Taxa de Câmbio a partir de {ano_inicio_filtro}', fontsize=18, fontweight='bold', fontname='Arial', pad=15)
matplt.xlabel('Ano', fontsize=12, fontweight='light', fontname='Arial',labelpad=15, loc = 'center')
matplt.ylabel('Taxa de Câmbio Média', fontsize=12, fontweight='light', fontname='Arial',labelpad=15, loc = 'center')

matplt.legend()
matplt.show()
