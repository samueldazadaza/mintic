def ordenes(rutinaContable):
    from functools import reduce
    total = list(map(lambda x: [x[0]]+list(map(lambda y:y[1]*y[2] ,x[1:])),rutinaContable)) #para recorrer lista
    total = list(map(lambda x: [x[0]]+[reduce(lambda a,b: round(a+b, 2) ,x[1:])],total)) #para redondear decimal a 2 cifras
    total = list(map(lambda x: x if x[1]>=600000 else [x[0], x[1]+25000] ,total)) #para aumentar los 25mil
    
    print('------------------------ Inicio Registro diario ---------------------------------')
    for i in range(len(total)):
        print(f'La factura {total[i][0]} tiene un total en pesos de {total[i][1]:,.2f}')
    print('-------------------------- Fin Registro diario ----------------------------------')
    
#copiar codigo en robot imaster de aqui hacia arriba

rutinaContable = [
    [6587, ("3268", 4, 25842.99), ("8274",18,23254.99), ("6548", 9, 48951.95), ("2547", 5, 8951.95)],
    [6588, ("1254", 3, 115362.58), ("9744", 2, 99235.66)],
]

ordenes(rutinaContable)