from mostrar import *
from validar import *

def inicio_app_dt(lista_dt):    
    
    while True:
        mostrar_menu()
        
        match seleccion_opcion():
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
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
    opcion = input('Ingrese Opcion: ')
    op_validado = validar_opcion(opcion)