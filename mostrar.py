import os
import re

def clean():
    os.system('cls')

def imprimir_dato(dato):
    print(dato)

def mostrar_menu():
    """ lista las opciones del menu principal"""
    imprimir_dato("""\n\t\t _____ MENU PRINCIPAL DREAM TEAM _____\n
    1) - Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
        'Nombre Jugador - Posición'.
    2) - Mostrar estadisticas de jugador seleccionado por indice.
    3) - Guardar las estadísticas del ultimo jugador seleccionado (Op.2) en un archivo CSV.
    4) - Buscar un jugador por su nombre y mostrar sus logros.
    5) - Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream
         Team, ordenado por nombre de manera ascendente.
    6) - Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es
         miembro del Salón de la Fama del Baloncesto.
    7) - Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
    8) - Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
    9) - Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.
    10) - Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
         más puntos por partido que ese valor.
    11)- Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
         más rebotes por partido que ese valor.
    12)- Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
         más asistencias por partido que ese valor.
    13)- Calcular y mostrar el jugador con la mayor cantidad de robos totales.
    14)- Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.
    15)- Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un
         porcentaje de tiros libres superior a ese valor.
    16)- Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al
         jugador con la menor cantidad de puntos por partido.
    17)- Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.
    18)- Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un
         porcentaje de tiros triples superior a ese valor.
    19)- Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas.
    20)- Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por
         posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a
         ese valor.
    21)- Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking.\n""")

def mostrar_jugador_posicion(dict_jugador:dict)->str:
    """ recibe un diccionario jugador y da formato al nombre junto a la posicion
    Args:
        dict_jugador (dict): informacion de un jugador
    Returns:
        texto_formato (str): string formateado con nombre y posicion del jugador"""
    texto_formato = '{0} - {1}'.format(dict_jugador['nombre'],dict_jugador['posicion'])
    return texto_formato

def mostrar_un_jugador(dict_jugador:dict)->str:
    """ muestras estadisticas de un jugador
    Args:
        dict_jugador (dict): datos del jugador
    Returns:
        texto_estadistica (str): texto formateado con toda la informacion listada"""
    texto_cabecera = 'nombre;posicion'
    texto_estadistica = '{0};{1}'.format(dict_jugador['nombre'],
                                                          dict_jugador['posicion'])
    print('\tESTADISTICA DE JUGADOR: {0}\n'.format(dict_jugador['nombre'].upper()))
    for estadistica in dict_jugador['estadisticas']:
        print('{0}: {1}'.format(estadistica,dict_jugador['estadisticas'][estadistica]))
        texto_cabecera += ';{0}'.format(estadistica)
        texto_estadistica += ';{0}'.format(dict_jugador['estadisticas'][estadistica])
    texto_final = '{0}\n{1}\n'.format(texto_cabecera,texto_estadistica)
    return texto_final

def mostrar_logros_jugador(dict_jugador:dict):
    """ lista logros de un jugador recibido por parametr
    Args:
        dict_jugador (dict): datos del jugador"""
    if not dict_jugador == '':
        print('\tLOGROS DE {0}\n'.format(dict_jugador['nombre'].upper()))
        for logro in dict_jugador['logros']:
            print('* {0}'.format(logro))       


def mostrar_promedio_por_partido_jugador(dict_jugador):
    """ muestra el romedio de puntos por partidos de un jugador
    Args:
        dict_jugador (dict): datos del jugador"""
    print('| {0:^20} |   {1:^12}   |'.format(dict_jugador['nombre'],
                        dict_jugador['estadisticas']['promedio_puntos_por_partido']))

def mostrar_jugador_salon_fama(dict_jugador):
    """ imprime por consola, de corresponder, si el jugador forma parte del salon de la fama
    Args:
        dict_jugador (dict): datos del jugador"""
    clean()
    if not dict_jugador == '':
        patron = r'\bfama\b|\bFama\b'
        print('- {0}\n'.format(dict_jugador['nombre'].upper()))
        for logros in dict_jugador['logros']:
            if bool(re.search(patron, logros)):
                print('- {0}'.format(logros))
                break
        else:
            print('- NO FORMA PARTE DEL SALOON DE LA FAMA')
        
def mostrar_jugadores_mayor_dato(lista_jugadores,key,dato, ingreso_usuario = False):
    """ Crea una lista diccionario con los jugadores que cumplen con la condicion, mostrando
    el de mayor dato, o mayor al dato ingresado por usuario.
    Args:
        lista_jugadores (list): lista de diccionarios de jugadores.
        key (str): criterio referencia sobre lo cual se evaluara.
        dato (int/float): valor base para evaluar
        ingreso_usuario (bool, optional): True, si el dato base a evaluar lo ingreso un usuario,
        False, si el dato surge del mayor valor de la lista"""
    maximo_jugador = []
    for dict_jugador in lista_jugadores:
        if (dict_jugador['estadisticas'][key] == dato and ingreso_usuario == False) or\
               (dict_jugador['estadisticas'][key] > dato and ingreso_usuario == True):
            maximo_jugador.append(dict_jugador)
    for jugador in maximo_jugador:
        print('| {0:^20} | {1:^5} |'.format(jugador['nombre'], jugador['estadisticas'][key]))
    
def mostrar_mayor_logro(lista_jugadores:list,mayor_logro:str):
    """ muestra en consola los jugadores que coinciden con el mayor logro recibido por
     parametro"""
    for jugador in lista_jugadores:
        if len(jugador['logros']) == mayor_logro:
            mostrar_logros_jugador(jugador)

def mostrar_tabla_ranking_jugadores(name:str,puntos:int,rebotes:int,asistencia:int,robos:int):
    """ imprime en consola la posicion de cada jugador respecto a las distintas estadisticas
    Args:
        name (str): nobre del jugador
        puntos (int): posicion en ranking de puntos
        rebotes (int): posicion en ranking de rebotes
        asistencia (int): posicion en ranking de asistencia
        robos (int): posicion en ranking de robos"""
    print('│ {0:^20} │ {1:^6} │ {2:^8} │ {3:^12} │ {4:^6} │'.format(name,puntos,rebotes,
                                                                    asistencia,robos))
