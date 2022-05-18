diccionario = {
	1: 80,
	2: "carlos"
}
print(diccionario)
# añadir con el metodo setdefault
diccionario.setdefault(3, True)
print(diccionario)
diccionario.setdefault(4, [5,7,8])
print(diccionario)

# añadir utilizando el operador de asignacion "="
diccionario[5] = "pedro"
print(diccionario)

for i in diccionario: 
        print(i)