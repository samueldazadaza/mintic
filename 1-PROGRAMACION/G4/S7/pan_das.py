import pandas as pd
df1 = pd.read_csv('surveys.csv')
print(df1)

print(df1.tail(8)) # imprime las ultimas n lineas
print(df1.shape)
print(df1.columns)
print(pd.unique(df1['species_id'])) # retorna una lista con los valores unicos de una columna
print(df1['species_id'].value_counts()) # cuenta la cantidad por valores unicos de una columna
print(df1['weight'].describe()) # devuelve datos de estadistica descriptiva
print(df1['weight'].max())
print(df1.groupby('species_id')['record_id'].count()['AH']) # aprupar por especies id, luego tomar el dato record id y contar valores
