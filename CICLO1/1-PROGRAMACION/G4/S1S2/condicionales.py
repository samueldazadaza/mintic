# Realice un programa que lea un numero entero y diga si es mayor o igual a 100
mensaje = "S"
while mensaje == "S":
    respuesta = input("Digite el numero:\n")
    numero1 = int(respuesta)
    if numero1 >= 100:
        print(f"El numero {numero1} es mayor o igual a 100")
    else:
        print(f"El numero: {numero1} es menor a 100")
    mensaje = input("presione S para continuar o cualquier tecla para salir")
