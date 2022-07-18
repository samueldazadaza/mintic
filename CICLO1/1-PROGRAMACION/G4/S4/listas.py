# Una lista es una colección de datos que se utiliza para guardar varios elementos
# Una lista es indexada de forma numerica
# Una lista es indexada de forma numérica
# Las listas son mutables

# crear listas:
ciudades = ["New York", "Londres", "Madrid", 89, True, 58.25, [9,0,8]]
frutas = list(("manzana", "pera", "coco")) # no olvide el doble parentesis si utilizamos el constructor
print(ciudades, type(ciudades))
print(frutas, type(frutas))
frutas[0] = "banana"
print(frutas)

for i in ciudades: # la variable i toma el valor de los elementos de la lista.
        if i == "Cali":
                print("Londres esta en la lista")
        print(i, type(i))
        
ciudades.append("caracas") # añadir elemento al final de la listas
ciudades.remove("New York") # eliminar elemento de lista
print(ciudades)

print("Londres" in ciudades)
ciudades.extend(frutas)
print(ciudades)

lista1 = ["carlos", 40, [50,20,80]]
print(lista1[2][1])

extraerElemento="caracas"
print(ciudades.index(extraerElemento))