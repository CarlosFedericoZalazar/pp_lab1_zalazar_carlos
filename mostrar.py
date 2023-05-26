import os
import re


def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


def imprimir_dato(dato):
    print(dato)

def mostrar_menu():
    imprimir_dato("""\t\t _____ MENU PRINCIPAL DREAM TEAM _____\n
    1) - Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
        'Nombre Jugador - Posición'.
    2) - Mostrar estadisticas de jugador seleccionado por indice.
    3) - Buscar un jugador por su nombre y mostrar sus logros.
    4) - Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream
         Team, ordenado por nombre de manera ascendente.
    5) - Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es
         miembro del Salón de la Fama del Baloncesto.\n""")

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
    texto_estadistica = '{0},{1}'.format(dict_jugador['nombre'],
                                                          dict_jugador['posicion'])
    print('\tESTADISTICA DE JUGADOR: {0}\n'.format(dict_jugador['nombre'].upper()))
    for estadistica in dict_jugador['estadisticas']:
        print('{0}: {1}'.format(estadistica,dict_jugador['estadisticas'][estadistica]))
        texto_estadistica += ',{0}'.format(estadistica,
                                    dict_jugador['estadisticas'][estadistica])
    texto_estadistica += '\n'
    return texto_estadistica

def mostrar_logros_jugador(dict_jugador:dict):
    """ lista logros de un jugador recibido por parametr
    Args:
        dict_jugador (dict): datos del jugador"""
    clean()
    if not dict_jugador == '':
        print('\tLOGROS DE {0}\n'.format(dict_jugador['nombre'].upper()))
        for logro in dict_jugador['logros']:
            print('* {0}'.format(logro))
        
    

def mostrar_promedio_por_partido(lista_jugadores):
    print('| {0:^20} |  {1:^12} |'.format('Nom. Jugador', 'Prom.Ptos.Part.'))
    print('-'* 43)
    for jugador in lista_jugadores:
        print('| {0:^20} |   {1:^12}   |'.format(jugador['nombre'], jugador['estadisticas']
                                                        ['promedio_puntos_por_partido']))

def mostrar_jugador_salon_fama(dict_jugador):
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
        


