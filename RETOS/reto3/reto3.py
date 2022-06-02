# Descripción
# Cadena de caracteres de la forma
# Producto consultado : {idProducto} Descripción {dProducto}
# Parte {pnProducto} Cantidad vendida {cvProducto} Stock
# {sProducto} Comprador {nComprador} Documento
# {cComprador} Fecha Venta {fVenta}
# Ó
# “No hay registro de venta de ese producto”

def Autopartes(ventas: list):
        diccionario = dict(zip(range(len(ventas)), ventas))
        return diccionario

def consultaRegistro(ventas: dict, idPoducto):
        #para preguntar en ventas si existe el producto
        for i in ventas:
                if ventas[i][0] == idProducto:
                        dProducto = ventas[i][1]
                        pnProducto = ventas[i][2]
                        cvProducto = ventas[i][3]
                        sProducto = ventas[i][4]
                        nComprador = ventas[i][5]
                        cComprador = ventas[i][6]
                        fVenta = ventas[i][7]
                        print(f"Producto consultado : {idProducto} Descripción {dProducto} Parte {pnProducto} Cantidad vendida {cvProducto} Stock {sProducto} Comprador {nComprador} Documento {cComprador} Fecha Venta {fVenta}")
        return f""
                # else:
                #         print("No hay registro de venta de ese producto")
                #print(ventas)

ventas = [
	(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
	(2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
	(2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
	(3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
	(9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')
]

print(consultaRegistro(Autopartes(ventas),2010))

#DE AQUI PARA ABAJO ES UNA PRUEBA ANTIGUA!!
"""
                        respuesta = f"Producto consultado : {idProducto} Descripción {dProducto} Parte {pnProducto} Cantidad vendida {cvProducto} Stock {sProducto} Comprador {nComprador} Documento {cComprador} Fecha Venta {fVenta}"
                # else:
                #         print("No hay registro de venta de ese producto")
                #print(ventas)
        return respuesta

"""
