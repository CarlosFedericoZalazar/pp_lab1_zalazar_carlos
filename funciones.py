from mostrar import *
from validar import *
import os

def pause():
    input('\nPresiones una tecla para continuar...')

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def separador():
    print('-'*70)

def inicio_app_dt(lista_dt):    
    
    while True:
        clean()
        mostrar_menu()
        
        match seleccion_opcion():
            case '1':
                clean()
                print('\t\t _____ LISTA JUGADORES _____\n')
                listar_jugadores_dt(lista_dt)
                pause()
            case '2':
                clean()
                print('\t\t _____ SELECCION DE JUGADOR _____\n')
                seleccionar_jugador_por_indice(lista_dt)
            case '3':
                print('OPCION ')
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

def listar_jugadores_dt(lista:list):
    """ lista jugadores con formato nombre y posicion
    Args:
        lista (list): lista datos de jugadores"""
    
    # for jugador in lista['jugadores']:
    #     print(mostrar_jugador_posicion(jugador))

    for indice in range(len(lista['jugadores'])):
        imprimir_dato('{0:>2}) {1}'.format(indice + 1, mostrar_jugador_posicion(lista['jugadores'][indice])))


def seleccionar_jugador_por_indice(lista_dt:list):
   
    listar_jugadores_dt(lista_dt)
    while True:
        indice_jugador = input('Ingrese indice de Jugador: ')
        indice_ok = validar_indice(indice_jugador,len(lista_dt['jugadores']))
        if indice_ok:
            break
    clean()
    indice_jugador = int(indice_jugador)
    mostrar_un_jugador(lista_dt['jugadores'][indice_jugador - 1])
    pause()

    
