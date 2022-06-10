# herencia
# existen varias relaciones entre las clases, una de ellas es la herencia
# se puede definir una clase que herede propiedades y metodos de otra clase.
# clase padre (clase principal, clase base), es aquella de la que se hereda
# clase hija (clase secundaria, clase derivada), es la clase que hereda

class Persona: #clase padre
    def __init__(self, nombre:str, apellido:str, edad:int):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def imprimir(self):
        print(self.nombre,self.apellido,self.edad)

x = Persona('Pedro', 'Martinez', 50) 
x.imprimir()

class Estudiante(Persona): # clase hija
    def saludo(self):
        print(f'Hola {self.nombre}, bienvenido!')

y = Estudiante('Ana', 'Cabrera', 35)
y.imprimir()
y.saludo()





  