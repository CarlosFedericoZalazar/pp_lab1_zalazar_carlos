from mostrar import *
from validar import *
from archivos import *
import os

def pause():
    input('\nPresiones una tecla para continuar...')

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def separador():
    print('-'*70)

def inicio_app_dt(dict_dt_jugadores: dict):
    '''
    '''    
    lista_check = [False,False,False]
    while True:
        clean()
        mostrar_menu()        
        match seleccion_opcion():
            case '1':
                clean()
                print('\t\t _____ LISTA JUGADORES _____\n')
                listar_jugadores_dt(dict_dt_jugadores['jugadores'])
                lista_check[0] = True
                pause()
            case '2':
                clean()
                print('\t\t _____ SELECCION DE JUGADOR _____\n')
                estadisticas = seleccionar_jugador_por_indice(dict_dt_jugadores['jugadores'])
                lista_check[1] = True
            case '3':
                buscar_jugador(dict_dt_jugadores['jugadores'])
            case '4':
                pass
            case '5':
                pass
            case '6':
                pass
            case '7':
                pass
            case another:
                print('Opcion equivocada')
                break

def seleccion_opcion():
    opcion_ok = False
    while True:
        opcion = input('Ingrese Opcion: ')
        op_validado = validar_opcion_ingresada(opcion)
        if op_validado:
            break
    return opcion

def listar_jugadores_dt(lista_jugadores:list):
    """ lista jugadores con formato nombre y posicion
    Args:
        lista (list): lista datos de jugadores"""
    for indice in range(len(lista_jugadores)):
        imprimir_dato('{0:>2}) {1}'.format(indice + 1, mostrar_jugador_posicion(lista_jugadores[indice])))

def seleccionar_jugador_por_indice(lista_jugadores:list):

    listar_jugadores_dt(lista_jugadores)
    while True:
        indice_jugador = input('Ingrese indice de Jugador: ')
        indice_ok = validar_indice(indice_jugador,len(lista_jugadores))
        if indice_ok:
            break
    clean()
    indice_jugador = int(indice_jugador)
    texto_estadistica = mostrar_un_jugador(lista_jugadores[indice_jugador - 1])
    while True:
         opcion_guardar = input('\nDesea guardar las estadisticas en un archivo? (S/N): ')
         opcion_ok = validar_s_n(opcion_guardar)
         if opcion_ok:
             break
         else:
             print('Error, caracter invalido. presiones S(si)/N(no)...')
    if opcion_ok:
        guardar_archivo_csv('{0}.csv'.format(lista_jugadores[indice_jugador - 1]['nombre']),
                                                                            texto_estadistica)
    return texto_estadistica

def buscar_jugador(lista_jugador:list):
    
    clean()
    print('Ingrese nombre del Jugador a buscar, o bien presiones "-" si desea salir.')
    while True:        
        nombre_jugador = input('Nombre a Buscar: ').capitalize()
        nombre_ok = validar_es_palabra(nombre_jugador)
        if nombre_ok or nombre_jugador == '-':
            break
        else:
            print('Error, ha ingresado caracteres invalidos. Intente nuevamente.')
            pause()
            clean()
    if not nombre_jugador == '-':
        nombre_ok = validar_busqueda_nombre(lista_jugador, nombre_jugador)
        if not nombre_ok:
             print('- NO HUBO COINCIDENCIAS EN SU BUSQUEDA -')
        pause()
        #break
