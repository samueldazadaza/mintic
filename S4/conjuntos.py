# Es una colección de datos que se utiliza para almacenar varios elementos.
# Los conjuntos no son odenados, son mutables. es decir se le pueden agregar o quitar elementos y no permite elementos duplicados.

#son parecidas a las LISTAS
#inicializar un conjunto FORMA 1
nombres = {
        "Juan",
        "Camilo",
        "Sergio",
        "veronica"
        }

#FORMA 2 crear conjunto
ciudades = set((
        "Caracas",
        "Panama",
        "Quito"
        ))
print(nombres, type(nombres))
print(ciudades, type(ciudades))
numeros = {8,9,4,7,3,5,7,6,1,3,8,4,0,3,4,8,6,3,5,7,8,23,1,777,5, True, "CasaCarlos"}
print(numeros)

# añadir elementos a un conjunto, metodo add
ciudades.add("Nueva York")

# Eliminar un elemento
ciudades.remove("Quito")
print(ciudades)

#recorrer elemento de conjunto
print("Panama" in ciudades)
for i in ciudades:
        print(i)
                