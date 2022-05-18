# las tuplas son una colección de datos que se utilizan para almacenar varios elementos
# son colecciones indexadas, son inmutables

# crear tupla
ciudades = ("Cali", "Medellin", "Barranquilla")
# ciudades[1] = "Monteria", esto NO se puede porque las tuplas son inmutables

# crear tupla se crea con parentesis
print(ciudades, type(ciudades))

#crear tupla opcion 2
datos = tuple()

# que pasa si quiero recorrer datos
"""
 reverse()
 append()
 extend()
 remove()
 clear()
 sort()
"""

for i in datos:
        print(i, type(i))

lista = list(datos)
print(lista, type(lista))

def operaciones(a,b):
        suma = a+b
        resta = a-b
        mult = a*b
        div = a/b
        return suma, resta, mult, div

resultados = operaciones(25,5)
print(resultados, type(resultados))
print(f"El resultado de la suma es: {resultados}")
