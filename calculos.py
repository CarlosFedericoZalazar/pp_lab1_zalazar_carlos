def calcular_promedio_puntos_partido(lista_jugadores):
    aucumulador_puntos = 0
    for jugador in lista_jugadores:
        aucumulador_puntos += jugador['estadisticas']['promedio_puntos_por_partido']
    promedio_puntos = aucumulador_puntos / len(lista_jugadores)
    print('\nEl promedio total de puntos por partido del equipo es: {0:.2f}\n'.format(promedio_puntos))

def calcular_mayor_dato(lista_jugadores, key):
    """ busca el mayor valor correspondiente  de una lista, respecto a una key recibida como
    parametro.
    Args:
        lista_jugadores (list): lista de diccionarios de jugadores
        key (str): clave sobre la cual determinara el criterio de la operacion
    Returns:
        dict_maximo (dict)_type_: diccionario del jugador con mayor valor encontrado"""
    mayor_dato = lista_jugadores[0]['estadisticas'][key]
    for dict_jugadores in lista_jugadores:
        if mayor_dato < dict_jugadores['estadisticas'][key]:
            mayor_dato = dict_jugadores['estadisticas'][key]
    return mayor_dato