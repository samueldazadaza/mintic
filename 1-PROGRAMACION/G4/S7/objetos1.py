










#crear clase
class Persona:
    def crear(self, nombre:str):
        self.name = nombre
        
    def mostrar(self)->str:
        return self.name
    
x = Persona() #aqui creamos el objeto
print(type(x))

x.crear('Maria')
x.name = 'Juan'
print(x.mostrar())








class Estudiante:
    def __init__(self):
        self.nombre = input('Digite el nombre del estudiante\n')
        self.nota = float(input('Digite la nota del estudiante\n'))
    def imprimir(self):
        print('Nombre: ', self.nombre)
        print('Nota: ', self.nota)
    def aprobar(self):
        if self.nota >= 3.0:
            print('Aprobo')
        else:
            print('No aprobo')

estudiante1 = Estudiante() #para crear el objeto
estudiante1.imprimir()
estudiante1.aprobar()





