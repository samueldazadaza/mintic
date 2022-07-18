def AutoPartes(ventas):
    diccionario = {}
    for i in ventas:
        if diccionario.get(i[0]) == None:
            diccionario[i[0]] = []
        diccionario[i[0]].append((i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
    return diccionario
        

def consultaRegistro(ventas,idProducto):
    if idProducto in ventas:
        for i in ventas[idProducto]:
            print(f'Producto consultado : {idProducto}  Descripción  {i[0]}  #Parte  {i[1]}  Cantidad vendida  {i[2]}  Stock  {i[3]}  Comprador {i[4]}  Documento  {i[5]}  Fecha Venta  {i[6]}')
    else:
        print('No hay registro de venta de ese producto')