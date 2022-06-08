import pandas as pd 

# ruta file csv
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'

def listaPeliculas(rutaFileCsv: str) -> str:
    tempo = rutaFileCsv.split('.')
    if 'csv' in tempo[-1]:
        try:
            df1 = pd.read_csv(rutaFileCsv)
            subdf1 = df1[["Country", "Language", "Gross Earnings"]] #subconjunto del dataframe con las columnas "Country", "Language" y "Gross Earnings".
            pt = pd.pivot_table(subdf1, index=["Country", "Language"]) # crear tabla dinamica de los 2 parametros: country y languaje.
            return pt.head(10) #tomar los 10 primeros registros de la tabla dinamica
        except:
            return f'Error al leer el archivo de datos.'
    else:
        return f'Extensión inválida.'

print(listaPeliculas(rutaFileCsv))

#en el bot del imaster-mintic subir todo el codigo anterior