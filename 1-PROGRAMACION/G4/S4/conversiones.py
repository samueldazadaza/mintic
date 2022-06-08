#borrar consola al principio
import os 
os.system ("cls") 

# cadenas a lista
cadena = "Colombia"
lista = list(cadena)
print(lista)
lista = "Venezuela 😀"
print(lista)

#lista a cadena
cad = '🟢'.join(lista)
print(cad)

# ej2
nombre = "Pedro"
diccionario = dict(zip(range(1, len(nombre)+1), nombre))
print(diccionario)

#ej3 diccionario 3
lista1 = ["Enero", "Febrero", "Marzo", "Abril"]
lista2 = [1500000, 2000000, 1800000, 2200000]
diccionario2 = dict(zip(lista1, lista2))
print(diccionario2)

#extraer valores
print(diccionario.values())
# extraer llaves
print(diccionario.keys())
# extraer lista de tuplas de items
print(diccionario.items())

#convertir a una cadena
cadena2 = ''.join(diccionario.keys())
print(cadena2)
