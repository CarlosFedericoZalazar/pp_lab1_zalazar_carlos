import re
from mostrar import *


def validar_opcion_ingresada(opcion):
    op_valida = False
    patron = r'[1-4]{1}$'
    if bool(re.match(patron, opcion)):
        print('opcion valida')
        op_valida = True
    else:
        print('malisimo')
    return op_valida

def validar_indice(indice:str,len_lista:int)->bool:
    opcion_ok = False
    if indice.isdigit():
        if int(indice) > 0 and int(indice) <= len_lista:
            opcion_ok = True
        else:
            print('- Error, indice fuera de rango. Intente nuevamente (0-{0})'.format(len_lista))
    else:
        print('- Error, no ha ingresado in digito valido. Intente nuevamente.')
    return opcion_ok

def validar_s_n(opcion:str)->bool:
    opcion_ok = False
    patron = r'[sS]$|[nN]$'
    if bool(re.match(patron,opcion)):
        opcion_ok = True
    return opcion_ok

def validar_busqueda_nombre(lista_jugadores:list, nombre_a_validar = '')->str:
    """ Realiza una busqueda mediante la escritura parcial o completa de un nombre en la lista
    recibida como parametro.
    Args:
        lista_jugadores (list): lista de jugadores
        nombre_a_validar (str, optional): _description_. Defaults to ''.

    Returns:
        str: _description_    """
   
    patron = nombre_a_validar.lower()
    matches = 0
    dict_nombre_encontrado = {}
    nombre_validado = False
    for i in range(len(lista_jugadores)):
        texto_auxiliar = lista_jugadores[i]['nombre'].lower()
        if bool(re.search(patron,texto_auxiliar)):
            matches += 1
            nombre_validado = lista_jugadores[i]['nombre']
            if matches == 1:                
                lista_coincidencias = [lista_jugadores[i]['nombre']]
                dict_nombre_encontrado = lista_jugadores[i]
                nombre_validado = True
            else:
                lista_coincidencias.append(lista_jugadores[i]['nombre'])
    if matches > 1:
        print('Se encontraron {0} coincidencias'.format(matches))
        for coincidencia in lista_coincidencias:
            print(coincidencia)
        nombre_a_validar = input('Escriba el nombre completo seleccionado: ')
        nombre_validado = validar_busqueda_nombre(lista_jugadores,nombre_a_validar)
    elif matches == 1:
        mostrar_logros_jugador(dict_nombre_encontrado)
    return nombre_validado

def validar_es_palabra(dato):
    patron = r'[a-zA-Z ]+'
    es_palabra = False
    if bool(re.match(patron,dato)):
        es_palabra=True
    return es_palabra   