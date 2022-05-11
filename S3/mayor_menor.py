# Realice un ejercicio que lea n numeros enteros y nos diga cual es mayor y el menor de ellos.
# Datos de entrada=> n: cantidad de numeros
# Realice                       numero: cada uno de los numeros ingresador por el usuario
# Datos de salida => mayor: el mayor numero
# Datos                      menor: el menor numero

n = int(input("Digite la cantidad de numeros que desea ingresar\n"))

for i in range(n): # la variable i va a contar desde 0 hasta n-1
        numero = int(input(f"Digite el numero {i+1}:\n"))
        if i == 0:
                mayor = numero
                menor = numero
        else:
                if numero > mayor:
                        mayor = numero
                if numero < menor:
                        menor = numero
print(f"El mayor de los {n} numeros ingresados es {mayor}")
print(f"El menor de los {n} numeros ingresados es {menor}")


