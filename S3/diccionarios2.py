datosPersonales = dict(
	nombre = 'Carlos',
 edad = 25,
 profesion = 'contador'
)
print(datosPersonales)

datosPersonales2 = {}
nombre = input('digite el nombre: \n')
datosPersonales2.setdefault('nombre', nombre)
edad = int(input('Digite la edad: \n'))
datosPersonales2.setdefault('edad', edad)
profesion = input('Digite la profesion: \n')
datosPersonales2.setdefault('profesion', profesion)

datosPersonales3 = {
	'nombre' : nombre,
	'edad' : edad,
	'profesion': profesion
}

print(datosPersonales2)
print(datosPersonales3)

#ejemplo inventario

inventario = {} # creamos un diccionario vacio
for i in range(3): # ejm. tengo un diccionario con las cantidades que tengo en existencia de los codigos de una tienda
        codigo = int(input('Digite el codigo del articulo👉: '))
        cantidad = int(input('Digite la cantidad existente👉: '))
        inventario.setdefault(codigo, cantidad)
        
print(inventario)

