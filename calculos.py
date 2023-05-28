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

def ordenamiento(lista:list,key:str, orden = True):
    lista_aux = lista[:]
    lista_de = []
    lista_iz = []
    if len(lista) <= 1:
       return lista_aux
    else:
        pivot = lista_aux[0]
        for elemento in lista_aux[1:]:
            if elemento[key] > pivot[key]:
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)  
   
    lista_iz = ordenamiento(lista_iz,key,True)
    lista_iz.append(pivot)
    lista_de = ordenamiento(lista_de,key,True)
    lista_iz.extend(lista_de)
    return lista_iz


def ordenamiento_estadistica(lista, key):
    lista_aux = lista[:]
    lista_de = []
    lista_iz = []
    if len(lista) <= 1:
       return lista_aux
    else:
        pivot = lista_aux[0]
        for elemento in lista_aux[1:]:
            if elemento['estadisticas'][key] < pivot['estadisticas'][key]:
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)     
    lista_iz = ordenamiento_estadistica(lista_iz,key)
    lista_iz.append(pivot)
    lista_de = ordenamiento_estadistica(lista_de,key)
    lista_iz.extend(lista_de)
    return lista_iz

def obtener_rankings(lista_jugadores,lista_puntos_ordenada,lista_rebotes_ordenada,
                                   lista_asistencia_ordenada, lista_robos_ordenada)->str:
    texto_auxiliar = 'Jugador,Puntos,Rebotes,Asistencias,Robos\n'

    for jugador in lista_jugadores:
        ranking_puntos = lista_puntos_ordenada.index(jugador)+ 1
        ranking_rebotes = lista_rebotes_ordenada.index(jugador) + 1
        ranking_asistencia = lista_asistencia_ordenada.index(jugador) + 1 
        ranking_robos = lista_robos_ordenada.index(jugador) + 1
        mostrar_tabla_ranking_jugadores(jugador['nombre'],ranking_puntos,ranking_rebotes,
                                                        ranking_asistencia,ranking_robos)
        texto_auxiliar += '{0},{1},{2},{3},{4}\n'.format(jugador['nombre'],ranking_puntos,
                                        ranking_rebotes,ranking_asistencia,ranking_robos)
    print('{0}{1}{2}'.format('└','─' * 66,'┘'))
    return texto_auxiliar