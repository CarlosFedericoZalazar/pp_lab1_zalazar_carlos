 
def prueba_app(lista_jugadores,key = ''):
    key = 'temporadas'
    lista_jug_auxiliar=[]
    dict_nombre={}

    for jugador in lista_jugadores:
        dict_nombre = {}        
        dict_nombre['nombre'] = jugador['nombre']
        dict_nombre[key] = jugador['estadisticas'][key]
        lista_jug_auxiliar.append(dict_nombre)
    

    for jugador in lista_jug_auxiliar:
        print(jugador['nombre'])
   # lista_jugadores = [{'nombre':'Magic Johnson','puntos_totales':8},{'nombre':'Magic Johnson','rebotes':8}]