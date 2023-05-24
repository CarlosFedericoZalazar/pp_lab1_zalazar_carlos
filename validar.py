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