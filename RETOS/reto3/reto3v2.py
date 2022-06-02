def AutoPartes(ventas):
    diccionario = {}
    for i in ventas: #recorriendo ventas
        if diccionario.get(i[0]) == None: #obtener valor y preguntar si es igual a none
            diccionario[i[0]] = [] #crear lista vacia del primer elemento encontrado
        diccionario[i[0]] = [] #CREAR LISTA VACIA QUE BUSCA EL CODIGO DEL PRODUCTO
        diccionario[i[0]].append((i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
    return diccionario
        
    

def consultaRegistro(ventas, idProducto):
    pass

#INGRESO DE DATOS EN LA FUNCION DEL BOT
ventas = [
	(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
	(2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
	(2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
	(3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
	(9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')
]

#print(consultaRegistro(Autopartes(ventas),2010))
print(AutoPartes(ventas))