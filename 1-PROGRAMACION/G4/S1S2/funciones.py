def saludo(): #definir la funcion
    print("hola mundo")
    print("Mision Tic 2022")

def suma(a,b): # a y b son los parametros de la función
    print(a+b)

#FUNCION SUMA
saludo() #llamar a la funcion
a = int(input("digite num1: "))
b = int(input("digite num2: "))
suma(a,b) # El 8 y 9 son los argumentos de la función

#RETORNO DE FUNCION
def resta(a,b):
    return a-b

print(resta(90,15))
