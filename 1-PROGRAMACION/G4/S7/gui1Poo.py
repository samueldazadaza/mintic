import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk() #Tk : ventana
        self.ventana1.title('Mini Calc')
        self.ventana1.mainloop()
        self.num1 = tk.StringVar()
        self.entrada1 = tk.Entry(self.Ventana1, width=10, textvariable=self.num1) # Entry : caja de texto
        
x = Aplicacion()