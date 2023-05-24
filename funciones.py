from mostrar import *
from validar import *



def inicio_app_dt(lista_dt):    
    
    while True:
        mostrar_menu()
        
        match seleccion_opcion():
            case '1':
                print('OPCION 1')
            case '2':
                print('OPCION 2')
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

def pause():
    input('Presiones una tecla para continuar...')