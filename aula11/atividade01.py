import pandas as pd 
# dicionário
filmes = {
    'Título': ['Zathura', '007', 'Diabo Veste Prada 2', 'Carros'],
    'Gênero': ['ação', 'comédia', 'animação', 'romance'], # ta guardando uma lista
    'Ano': [2005, 2006, 2021, 2026]
}

#Pandas
# ----------------------------------------------------------------------

print('\nDATAFRAME (PANDAS): ') # dataframe é tipo um excel/tabela no python 
print(30*'-')
df_filmes = pd.DataFrame(filmes)

print(df_filmes) # Imprimindo os filmes
print()
print(df_filmes['Título']) # Imprimindo um Gênero específico
print()
print(df_filmes['Gênero']) # Imprimindo um Gênero específico
print()
print(df_filmes['Ano']) # Imprimindo um Gênero específico


