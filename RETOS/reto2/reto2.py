def cliente(informacion:dict):
        if informacion['primer_ingreso'] == False:
                total_boleta = 'N/A'
        if informacion['edad'] > 18:
                atraccion = 'X-Treme'
                apto = True
                total_boleta = (20000 * 0.95)
        elif informacion['edad'] >= 15 and informacion['edad'] <=18:
                atraccion = 'Carros chocones'
                apto = True
                total_boleta = (5000 * 0.93)
        elif informacion['edad'] >= 7 and informacion['edad'] <= 15:
                atraccion = 'Sillas voladoras'
                apto = True
                total_boleta = (10000 * 0.95)
        else:
                atraccion = 'N/A'
                apto = False
                total_boleta = 'N/A'
        
        info2 = {
		'nombre' : informacion['nombre'],
		'edad' : informacion['edad'],
		'atraccion' : atraccion,
		'apto': apto,
		'primer_ingreso': informacion['primer_ingreso'],
		'total_boleta': total_boleta
	}
        return info2

informacion = {
	'id_cliente':1,
	'nombre': 'Tatiana Ruiz',
	'edad': 2,
	'primer_ingreso': True
}

print(cliente(informacion))