import re
from mostrar import *


def validar_opcion_ingresada(opcion:str)->bool:
    """ valida la opcion ingresada en el menu principal
    Args:
        opcion (str): opcion ingresada por el usuario
    Returns:
        op_valida (bool): True si la opcion es valida, False caso contrario."""
    op_valida = False
    if opcion.isdigit() or opcion == '-':
        op_valida = True
    return op_valida

def validar_indice(indice:str,len_lista:int)->bool:
    """ valida que el indice ingresado por el usuario se un digito y a su vez que el mismo
    se encuentre dentro del rango de una lista.
    Args:
        indice (str): indice a validar ingresado por usuario
        len_lista (int): cantidad de elementos de una lista
    Returns:
        indice_ok (bool): True si el indice cumple con las condiciones, False caso contrario."""
    indice_ok = False
    if indice.isdigit():
        if int(indice) > 0 and int(indice) <= len_lista:
            indice_ok = True
        else:
            print('- Error, indice fuera de rango. Intente nuevamente (0-{0})'.format(len_lista))
    else:
        print('- Error, no ha ingresado in digito valido. Intente nuevamente.')
    return indice_ok

def validar_s_n(opcion:str)->bool:
    """ valida que el usuario halla ingresaado 's' o 'n' como opcion
    Args:
        opcion (str): opcion ingresada por el usuario
    Returns:
        opcion_ok (bool): True si resulta valida la operacion, False caso contrario"""
    opcion_ok = False
    patron = r'[sS]$|[nN]$'
    if bool(re.match(patron,opcion)):
        opcion_ok = True
    return opcion_ok

def validar_busqueda_nombre(lista_jugadores:list, nombre_a_validar:str)->dict:
    """ Realiza una busqueda mediante la escritura parcial o completa de un nombre en la lista
    recibida como parametro.
    Args:
        lista_jugadores (list): lista de jugadores
        nombre_a_validar (str): nombre a buscar en la lista de jugadores.
    Returns:
        nombre_validado (bool): True si pudo hacer la operacion, False caso contrario."""   
    patron = nombre_a_validar.lower()
    matches = 0
    dict_nombre_encontrado = {}
    #nombre_validado = False
    for i in range(len(lista_jugadores)):
        texto_auxiliar = lista_jugadores[i]['nombre'].lower()
        if bool(re.search(patron,texto_auxiliar)):
            matches += 1
            #nombre_validado = lista_jugadores[i]['nombre']
            if matches == 1:                
                lista_coincidencias = [lista_jugadores[i]['nombre']]
                dict_nombre_encontrado = lista_jugadores[i]
                #nombre_validado = True
            else:
                lista_coincidencias.append(lista_jugadores[i]['nombre'])
    if matches > 1:
        print('Se encontraron {0} coincidencias'.format(matches))
        for coincidencia in lista_coincidencias:
            print(coincidencia)
        nombre_a_validar = input('Escriba el nombre completo seleccionado: ')
        dict_nombre_encontrado = validar_busqueda_nombre(lista_jugadores,nombre_a_validar)
    return dict_nombre_encontrado

def validar_es_palabra(dato):
    """ valida si un dato es palabra valida
    Args:
        dato (str): dato a validar
    Returns:
        es_palabra (bool): True si es palabra valida, False caso contrario."""
    patron = r'[a-zA-Z ]+'
    es_palabra = False
    if bool(re.match(patron,dato)):
        es_palabra=True
    return es_palabra

def validar_numero_a_parsear(numero)->bool:
    """ verifica a traves de una expresion si el numero es float o entero, posible de castear
    Args:
        numero (str): numero a evaluar ingresado por usuario
    Returns:
        numero_ok (bool): True si es numero valido, False caso contrario."""
    numero_ok = False
    patron = r'^[0-9]+.[0-9]+$|[0-9]+$'
    if bool(re.match(patron,numero)) and float(numero) > 0:
        numero_ok = True
    return numero_ok