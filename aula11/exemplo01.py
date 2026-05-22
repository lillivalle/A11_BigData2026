import pandas as pd 
# dicionário
dados = {
    'Cargos': ['assistente', 'auxiliar', 'gerente'],
    'Salários': [2500, 1800, 7500] # ta guardando uma lista
}

print('\nInformações dos Funcionários: ')
print(30* '-')
print(dados)
print(dados['Cargos'])
#print(dados['salários'][0]) # [0] é o primeiro item da lista
print(dados['Salários'][2]) # Imprimindo um salário específico

#Pandas 
# --------------------------------------------------------------
print('\nDATAFRAME (PANDAS): ')
print(30*'-')
df_dados = pd.DataFrame(dados) # agora o pandas eu to chamando de pd 
# e o DataFrame é uma maneira de representar e trabalhar com dados tabulares
print(df_dados['Cargos'])
print(df_dados['Salários'].sum()) # Total
print(df_dados['Salários'].max()) # Maior 
print(df_dados['Salários'].min()) # Menor
print(df_dados['Salários'].mean()) # Média
