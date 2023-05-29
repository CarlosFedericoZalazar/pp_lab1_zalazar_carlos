from mostrar import *
from archivos import *


def calcular_promedio_puntos_partido(lista_jugadores:list, total_equipo = True, min_dato:float = 0):
    """ calcula promedio de puntos por partido del equipo, o bien descartando a los que tengan
    menor rendimiento segun criterio ingresado por parametro]
    Args:
        lista_jugadores (list): lista completa del equipo
        total_equipo (bool, optional): True si la operacion es sobre el total del equipo, False
        en caso de descratar a los de menor rendimiento.
        min_dato (float): minimo dato promedio, en caso de no ser requerido default '0'."""
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

def ordenamiento(lista:list,key:str):
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

def obtener_rankings(lista_jugadores:list,lista_puntos_ordenada:list,lista_rebotes_ordenada:list,
                                lista_asistencia_ordenada:list, lista_robos_ordenada:list)->str:
    """ obtiene la posicion en el ranking de los distintos jugadores
    Args:
        lista_jugadores (list): lista completa de los jugadore
        lista_puntos_ordenada (list): lista ordenada ascendente por puntos
        lista_rebotes_ordenada (list): lista ordenada ascendente por rebotes
        lista_asistencia_ordenada (list): lista ordenada ascendente por asistencia
        lista_robos_ordenada (list): lista ordenada ascendente por robos
    Returns:
        texto_auxiliar (str): retorna un texto con toda la informacion obtenida.
    """
    texto_auxiliar = 'Jugador;Puntos;Rebotes;Asistencias;Robos\n'
    for jugador in lista_jugadores:
        ranking_puntos = lista_puntos_ordenada.index(jugador)+ 1
        ranking_rebotes = lista_rebotes_ordenada.index(jugador) + 1
        ranking_asistencia = lista_asistencia_ordenada.index(jugador) + 1 
        ranking_robos = lista_robos_ordenada.index(jugador) + 1
        mostrar_tabla_ranking_jugadores(jugador['nombre'],ranking_puntos,ranking_rebotes,
                                                        ranking_asistencia,ranking_robos)
        texto_auxiliar += '{0};{1};{2};{3};{4}\n'.format(jugador['nombre'],ranking_puntos,
                                        ranking_rebotes,ranking_asistencia,ranking_robos)
    print('{0}{1}{2}'.format('└','─' * 66,'┘'))
    return texto_auxiliar

def calcular_posicion_ranking_jugadores(lista_jugadores:list):
    """ ordena los jugadores para introducirlos a la tabla de rankings y la muestra.
    Genera un archivo csv con la informacion obtenida.
    Args:
        lista_jugadores (list): tipo de eestadistica a listar"""
    clean()
    print('\t\t --- TABLA RANKING JUGADORES DREAM TEAM ---\n')
    print('{0}{1}{2}'.format('┌','─' * 66,'┐'))    
    print('│ {0:^20} │ {1:^6} │ {2:^8} │ {3:^12} │ {4:^6} │'.format('Jugador','Puntos',
                                                        'Rebotes','Asistencias','Robos'))
    print('{0}{1}{2}'.format('├','─' * 66,'┤'))    
    lista_puntos_ordenada = ordenamiento_estadistica(lista_jugadores,'puntos_totales') 
    lista_rebotes_ordenada = ordenamiento_estadistica(lista_jugadores,'rebotes_totales')
    lista_asistencia_ordenada = ordenamiento_estadistica(lista_jugadores,'asistencias_totales')
    lista_robos_ordenada = ordenamiento_estadistica(lista_jugadores,'robos_totales')
    tabla_str = obtener_rankings(lista_jugadores, lista_puntos_ordenada, lista_rebotes_ordenada,
                                    lista_asistencia_ordenada, lista_robos_ordenada)
    guardar_archivo_csv('ranking_jugadores.csv',tabla_str)
    