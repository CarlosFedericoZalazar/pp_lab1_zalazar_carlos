from mostrar import *

def calcular_promedio_puntos_partido(lista_jugadores, total_equipo = True, min_dato=''):
    acumulador_puntos = 0
    cantidad_promedio = len(lista_jugadores)
    for jugador in lista_jugadores:
        if (total_equipo == False) and (min_dato == jugador['estadisticas']
                                           ['promedio_puntos_por_partido']):
            cantidad_promedio -= 1
            continue
        if total_equipo == False: 
            mostrar_promedio_por_partido_jugador(jugador)
        acumulador_puntos += jugador['estadisticas']['promedio_puntos_por_partido']       
    promedio_puntos = calculo_promedio(acumulador_puntos, cantidad_promedio)
    if total_equipo:
        print('\nPromedio total de puntos por partido del equipo es: {0:.2f}\n'.format
                                                                        (promedio_puntos))
    else:
        print('\nPromedio Ptos. p/partido exceptuando al jugador con menor puntos es: {0:.2f}\n'
                                                                      .format(promedio_puntos))


def calcular_mayor_menor_dato(lista_jugadores, key, mayor = True):
    """ busca el mayor valor correspondiente  de una lista, respecto a una key recibida como
    parametro.
    Args:
        lista_jugadores (list): lista de diccionarios de jugadores
        key (str): clave sobre la cual determinara el criterio de la operacion
    Returns:
        dict_maximo (dict)_type_: diccionario del jugador con mayor valor encontrado"""
    may_men_dato = lista_jugadores[0]['estadisticas'][key]
    for dict_jugadores in lista_jugadores:
        if (may_men_dato < dict_jugadores['estadisticas'][key] and mayor == True) or\
               (may_men_dato > dict_jugadores['estadisticas'][key] and mayor == False):
            may_men_dato = dict_jugadores['estadisticas'][key]
    return may_men_dato

def calculo_promedio(numero,cantidad):
    promedio = numero / cantidad
    return promedio

def calcular_mayor_logro(lista_jugadores:list)->int:
    """ recibe una lista y establece la mayor cantidad de logros que tiene un jugador en la
    lista
    Args:
        lista_jugadores (list): lista de diccionario de jugadores
    Returns:
        mayor_logro (int): mayor cabtidad de logros encontrada en la lista"""
    mayor_logro = len(lista_jugadores[0]['logros'])
    for jugador in lista_jugadores[1:]:
        if mayor_logro < len(jugador['logros']):
            mayor_logro = len(jugador['logros'])
    return mayor_logro