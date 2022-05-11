class Vengador:
    def  name(self, codifica_nombre, nombre_real):
                    self.codifica_nombre = codifica_nombre
                    self.nombre_real = nombre_real
                    self.poder=poder
                    self.eslogan=eslogan
                    self.password="Identidad"
                    
    def introduce_self(self):
        return    "¡Hola mi nombe es {} y mi especialidad es {}".format(self.codifica_nombre,self.poder)
   
    def  decir_frase(self):
        return self.eslogan
   
    def revelar_Identidad (self):
        for i in range(3):      
        password = input("ingresa la contraseña: ").strip()
    if password == self.password:
        return "El verdadero nombre de {} es... {}. ¡no se lo digas a nadie!".format(self.codifica_nombre, self.nombre_real)
    else:
        print("lo siento debe conocer la contraseña para conocer la identidad de {}".format(se))
    Vengador1 = Vengador("capitan America","poder","escudo")
    Vengador2 = Vengador("thor","fuerza","mazo")
    Vengador3 = Vengador("30","20","25")                  