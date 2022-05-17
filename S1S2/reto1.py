def CDT(usuario:str, capital:int, tiempo:int):
	porcentaje_interes = 0.03
	porcentaje_a_perder = 0.02
	if tiempo > 2:
		valor_interes = (capital * porcentaje_interes * tiempo)/12
		valor_total = (valor_interes + capital)
		return f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}'
	if tiempo <=2:
		valor_a_perder = (capital * porcentaje_a_perder)
		valor_total_negativo = (capital - valor_a_perder)
		return f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total_negativo}'

"""
print(CDT('AB1012', 1000000, 3))
print(CDT('ER3366', 650000, 2))
print(CDT('ER1066', 1000000, 2))
"""