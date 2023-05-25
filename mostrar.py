def imprimir_dato(dato):
    print(dato)

def mostrar_menu():
    imprimir_dato("""
    1) - Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
        'Nombre Jugador - Posición'.
    2) - Mostrar estadisticas de jugador seleccionado por indice.
    3) - Guardar las estadísticas de ese jugador en un archivo CSV.
    4) -""")

def mostrar_jugador_posicion(dict_jugador:dict)->str:
    """ recibe un diccionario jugador y da formato al nombre junto a la posicion
    Args:
        dict_jugador (dict): informacion de un jugador
    Returns:
        texto_formato (str): string formateado con nombre y posicion del jugador"""
    texto_formato = '{0} - {1}'.format(dict_jugador['nombre'],dict_jugador['posicion'])
    return texto_formato


def mostrar_un_jugador(dict_jugador:dict)->str:
    texto_estadistica = '{0},{1}'.format(dict_jugador['nombre'],
                                                          dict_jugador['posicion'])
    print('\tESTADISTICA DE JUGADOR: {0}\n'.format(dict_jugador['nombre'].upper()))
    for estadistica in dict_jugador['estadisticas']:
        print('{0}: {1}'.format(estadistica,dict_jugador['estadisticas'][estadistica]))
        texto_estadistica += ',{0}'.format(estadistica,
                                    dict_jugador['estadisticas'][estadistica])
    texto_estadistica += '\n'
    return texto_estadistica