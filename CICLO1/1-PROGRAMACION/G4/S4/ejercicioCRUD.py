# Realice un programa que lea el código de un producto como llave de un 
# diccionario y en dicha llave va a almacenar nombre, precio y cantidad 
# del producto en una lista.
# Ejemplo

# El programa debe permitir cargar datos al diccionario, debe mostrar 
# un listado completo del diccionario, debe permitir consultar un producto 
# por su llave, actualizar precio y/o cantidad de un producto
# y eliminar productos

# Aplicación CRUD, create, read, update, delete
def crear():
        codigo = int(input("Digite el codigo del producto👉: "))
        nombre = input("Digite el nombre del producto👉: ")
        precio = int(input("Digite el precio unitario del producto👉: "))
        cantidad = int(input("Digite la cantidad existente👉: "))
        #productos.setdefault(codigo, [nombre, precio, cantidad]) #añadir una llave
        productos[codigo] = [nombre, precio, cantidad]
        print("Producto creado: ", productos[codigo])

def mostrar():
        print("LISTADO DE PRODUCTOS")
        print("Codigo", "Nombre", "Precio", "Cantidad", sep="\t\t")
        for i in productos:
                print(i, productos[i][0], productos[i][1], productos[i][2], sep="\t\t")

def consultar():
        codigo = int(input("Digite el codigo del producto que desea consultar👉: "))
        if codigo in productos:
                print("Codigo", "Nombre", "Precio", "Cantidad", sep="\t\t")
                print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2], sep="\t\t")

        else:
                print("El codigo del producto no existe")

def actualizar():
        # actualizar precio y cantidad
        codigo = int(input("Digite el codigo del producto que desea actualizar👉: "))
        if codigo in productos:
                precio = int(input("Digite el nuevo precio del producto👉: "))
                cantidad = int(input("Digite la cantidad actualizada del producto👉: "))
                productos[codigo][1] = precio
                productos[codigo][2] = cantidad
                print("Producto actualizado", productos[codigo])
        else:
                print("El codigo del producto NO existe")

def borrar():
        codigo = int(input("Digite el codigo del producto que desea eliminar👉: "))
        if codigo in productos:
                print("Producto eliminado", productos.pop(codigo))
        else:
                print("El codigo del producto NO existe")

productos = { #Inicializar el diccionario
	1: ["manzana", 2500, 60],
	2: ["pera", 2800, 85],
	3: ["banana", 500, 680]
}

continuar = "s"
while continuar == "s" or continuar == "S":
	try:
		print("Menu")
		print("1. Crear")
		print("2. Mostrar")
		print("3. Consultar")
		print("4. Actualizar")
		print("5. Eliminar")
		opcion = int(input("Digite una opción: [1/2/3/4/5]👉👉: "))
		if opcion == 1:
			crear()
		elif opcion == 2:
			mostrar()
		elif opcion == 3:
			consultar()
		elif opcion == 4:
			actualizar()
		elif opcion == 5:
			borrar()
		else:
			print("Digite una opcion valida")
	except:
		print("❗❗Digite una opcion valida: 1,2,3,4 o 5")
	continuar = input('🟢Digite "s" para continuar o cualquier tecla para salir')