# Aqui vamos criar um gráfico de linha para mostrar os valores máximos e mínimos anuais da taxa de câmbio
# Calculamos os valores máximos e mínimos anuais da Taxa de Câmbio
df_extremos = df_dados.groupby('Ano')['Taxa Câmbio'].agg(['max', 'min']).reset_index()

# Convertemos 'Ano' para datetime para facilitar a plotagem
df_extremos['Ano'] = df_extremos['Ano'].dt.to_timestamp()

# Criamos o gráfico
# Solicitar ao usuário o ano de início
ano_inicio_filtro = int(input("Digite o ano de início para visualizar os dados (ex: 2020): "))

# Filtrar os dados a partir do ano escolhido pelo usuário
df_extremos = df_extremos[df_extremos['Ano'].dt.year >= ano_inicio_filtro]

# Aqui são as configurações de plot para os valores máximos e mínimos anuais da taxa de câmbio
matplt.figure(figsize=(12,7))
matplt.plot(df_extremos['Ano'], df_extremos['max'], marker='o', linestyle='-', label='Máximo Anual', color='blue')
matplt.plot(df_extremos['Ano'], df_extremos['min'], marker='o', linestyle='-', label='Mínimo Anual', color='gray')

# Adiciona os valores máximos e mínimos no gráfico
for i, row in df_extremos.iterrows():
    matplt.text(row['Ano'], row['max'] + 0.02, f"{row['max']:.2f}", fontsize=9, ha='center', va='bottom', color='black', fontname='Arial', fontweight='light')
    matplt.text(row['Ano'], row['min'] + 0.02, f"{row['min']:.2f}", fontsize=9, ha='center', va='bottom', color='black', fontname='Arial', fontweight='light')

# Configurações do título do gráfico
matplt.title('Máximos e Mínimos Anuais da Taxa de Câmbio', fontsize=18, fontweight='bold', fontname='Arial', pad=15)

#Configurações dos eixos e grid
matplt.xlabel('Ano', fontsize=12, fontname='Arial', labelpad=15, loc='center')
matplt.ylabel('Taxa de Câmbio', fontsize=12, fontname='Arial', labelpad=15, loc='center')
matplt.grid(True, linestyle='dotted', color='gray', alpha=0.2)
matplt.legend()
matplt.show()
