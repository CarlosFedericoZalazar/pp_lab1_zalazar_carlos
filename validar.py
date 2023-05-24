import re


def validar_opcion_ingresada(opcion):
    op_valida = False
    patron = r'[1-4]{1}$'
    if bool(re.match(patron, opcion)):
        print('opcion valida')
        op_valida = True
    else:
        print('malisimo')
    

    return op_valida