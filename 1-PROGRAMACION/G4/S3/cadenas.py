# las cadenas son idexadas de forma numérica
# las cadenas son inmutables
lenProg = "Python"
print(lenProg[3])
print(lenProg[-1])
lenProg = "Javascript....."
print(lenProg)
# lenProg[0] = "p" // esto NO se puede, las cadenas son inmutables
print(len(lenProg)) # ver longitud de cadena de texto
print(lenProg[4])
cadenaVacia = ""
print(len(cadenaVacia))
print(lenProg.count("a"))
fruta = 'manzana'
print(fruta[2:5])
print(fruta[:5])
print(fruta[2:])
print(fruta[2:5:2])
print(fruta.replace("a", "@"))

for i in fruta: # la variable i va tomando los valores de los caracteres de fruta
        print(i)




