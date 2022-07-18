def cliente(informacion:dict):
        xtreme = 20000
        carros_chocones = 5000
        sillas_voladoras = 10000
        if informacion['edad'] > 18:
                atraccion = 'X-Treme'
                apto = True
                if informacion['primer_ingreso'] == True:
                        total_boleta = (xtreme * 0.95)
                else:
                        total_boleta = xtreme
        elif informacion['edad'] >= 15 and informacion['edad'] <=18:
                atraccion = 'Carros chocones'
                apto = True
                if informacion['primer_ingreso'] == True:
                        total_boleta = (carros_chocones * 0.93)
                else:
                        total_boleta = carros_chocones
        elif informacion['edad'] >= 7 and informacion['edad'] <= 15:
                atraccion = 'Sillas voladoras'
                apto = True
                if informacion['primer_ingreso'] == True:
                        total_boleta = (sillas_voladoras * 0.95)
                else:
                        total_boleta = sillas_voladoras
        else:
                atraccion = 'N/A'
                apto = False
                total_boleta = 'N/A'
        
        info2 = {
		'nombre':informacion['nombre'],
		'edad':informacion['edad'],
		'atraccion':atraccion,
		'apto':apto,
		'primer_ingreso':informacion['primer_ingreso'],
		'total_boleta':total_boleta
	}
        return info2

#En el bot pegar de aqui hacia arriba
"""

informacion1 = {
	'id_cliente':1,
	'nombre': 'Johana Fernandez',
	'edad': 20,
	'primer_ingreso': True
}
informacion2 = {
	'id_cliente':1,
	'nombre': 'Johana Fernandez',
	'edad': 20,
	'primer_ingreso': False
}
informacion3 = {
	'id_cliente':2,
	'nombre': 'Gloria Suarez',
	'edad': 3,
	'primer_ingreso': True
}
informacion4 = {
	'id_cliente':3,
	'nombre': 'Tatiana Suarez',
	'edad': 17,
	'primer_ingreso': True
}
informacion5 = {
	'id_cliente':3,
	'nombre': 'Tatiana Suarez',
	'edad': 17,
	'primer_ingreso': False
}
informacion6 = {
	'id_cliente':4,
	'nombre': 'Tatiana Ruiz',
	'edad': 8,
	'primer_ingreso': True
}
informacion7 = {
	'id_cliente':1,
	'nombre': 'Tatiana Ruiz',
	'edad': 8,
	'primer_ingreso': False
}

print(cliente(informacion1))
print(cliente(informacion2))
print(cliente(informacion3))
print(cliente(informacion4))
print(cliente(informacion5))
print(cliente(informacion6))
print(cliente(informacion7))

"""