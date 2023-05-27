from mostrar import *
from validar import *
from archivos import *
from calculos import *
import os

def pause():
    input('\nPresiones una tecla para continuar...')

def clean():
    os.system('cls') # 'clear' para Linux
   

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
                buscar_mostrar_logros(dict_dt_jugadores['jugadores'])
            case '4':
                clean()
                print('\t\t _____ PROMEDIOS POR PARTIDO _____\n')
                calcular_mostrar_promedio(dict_dt_jugadores['jugadores'])
                pause()
            case '5':
                verificar_jugador_salon_fama(dict_dt_jugadores['jugadores'])                
            case '6':
                calcular_mostrar_cantidad_mayor(dict_dt_jugadores['jugadores'],
                                                             'rebotes_totales')
            case '7':
                calcular_mostrar_cantidad_mayor(dict_dt_jugadores['jugadores'],
                                                   'porcentaje_tiros_de_campo')
            case '8':
                calcular_mostrar_cantidad_mayor(dict_dt_jugadores['jugadores'],
                                                         'asistencias_totales')
            case '9':
                ingresar_mostrar_mayor_promedio(dict_dt_jugadores['jugadores'],
                                               'promedio_puntos_por_partido',9)
            case '10':
                ingresar_mostrar_mayor_promedio(dict_dt_jugadores['jugadores'],
                                                            'robos_totales',10)
            case '11':
                ingresar_mostrar_mayor_promedio(dict_dt_jugadores['jugadores'],
                                         'promedio_asistencias_por_partido',11)
            case '12':
                calcular_mostrar_cantidad_mayor(dict_dt_jugadores['jugadores'],
                                                             'rebotes_totales')
            case '13':
                calcular_mostrar_cantidad_mayor(dict_dt_jugadores['jugadores'],
                                                            'bloqueos_totales')
            case '14':
                ingresar_mostrar_mayor_promedio(dict_dt_jugadores['jugadores'],
                                                'porcentaje_tiros_de_campo',14)
            case '15':
                pass
            case other:
                print('Opcion equivocada')          
            

def seleccion_opcion():
    """ ingresa la opcion la opcion ingresada por el usuario
    Returns:
        opcion (str): opcion seleccionada, ya validada."""
    opcion = input('Ingrese Opcion: ')
    op_validado = validar_opcion_ingresada(opcion)
    if not op_validado:
        print('Ha ingresado un caracter invalido. Intente nuevamente...')
        pause()
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
    dict_nombre_jugador={}
    print('\nIngrese nombre del Jugador a buscar, o bien presiones "-" si desea salir.')
    while True:        
        nombre_jugador = input('Nombre a Buscar: ').capitalize()
        nombre_ok = validar_es_palabra(nombre_jugador)
        if nombre_ok or nombre_jugador == '-':
            break
        else:
            print('Error, ha ingresado caracteres invalidos. Intente nuevamente.')
    if not nombre_jugador == '-':
        dict_nombre_jugador = validar_busqueda_nombre(lista_jugador, nombre_jugador)
        if len(dict_nombre_jugador) == 0:
             print('- NO HUBO COINCIDENCIAS EN SU BUSQUEDA -')
             pause()
    return dict_nombre_jugador

def ordenamiento(lista:list,orden = True):
    lista_aux = lista[:]
    lista_de = []
    lista_iz = []
    if len(lista) <= 1:
       return lista_aux
    else:
        pivot = lista_aux[0]
        for elemento in lista_aux[1:]:
            if elemento['nombre'] > pivot['nombre']:
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)  
   
    lista_iz = ordenamiento(lista_iz,True)
    lista_iz.append(pivot)
    lista_de = ordenamiento(lista_de,True)
    lista_iz.extend(lista_de)
    return lista_iz

def calcular_mostrar_promedio(lista_jugadores:list)->list:
    """ calcula promedio de puntos por partido total del equipo, y muestra el de los jugadores
    ordenados de manera alfabetica
    Args:
        lista_jugadores (list): lista de los jugadores
    Returns:
        list: _description_"""
    lista_ordenada = ordenamiento(lista_jugadores)
    mostrar_promedio_por_partido(lista_ordenada)
    calcular_promedio_puntos_partido(lista_ordenada)
    
def buscar_mostrar_logros(lista_jugadores):
    dict_jugador = buscar_jugador(lista_jugadores)
    if not len(dict_jugador) == 0:
        mostrar_logros_jugador(dict_jugador)
        pause()

def verificar_jugador_salon_fama(lista_jugadores):
    clean()
    listar_jugadores_dt(lista_jugadores)
    dict_jugador = buscar_jugador(lista_jugadores)
    separador()
    if not len(dict_jugador) == 0:
        mostrar_jugador_salon_fama(dict_jugador)
        pause()

def calcular_mostrar_cantidad_mayor(lista_jugadores:list, key:str):
    mayor_dato = calcular_mayor_dato(lista_jugadores,key)
    clean()
    key_formateada = key.replace('_',' ').upper()
    print('\t___ Jugador/es con mayor {0} ___\n'.format(key_formateada))
    print('| {0:^20} | {1:^5} |'.format('NOMBRE', 'CANT.'))
    mostrar_jugadores_mayor_dato(lista_jugadores,key,mayor_dato)
    pause()
    pass

def ingresar_mostrar_mayor_promedio(lista_jugadores:list, key:str, opcion):
    clean()
    print('\t\t__ OPCION {0} __\n'.format(opcion))
    mayor_dato = calcular_mayor_dato(lista_jugadores,key)
    dato_usuario = input('Ingrese valor ({0} es el mayor numero):'.format(mayor_dato))
    numero_ok = validar_numero_a_parsear(dato_usuario)
    if numero_ok:
        dato_usuario = float(dato_usuario)
        if dato_usuario < mayor_dato:
            clean()
            key_formateada = key.replace('_',' ').upper()
            print('\t\t JUGADOR/ES CON MAYOR {0}\n'.format(key_formateada))
            print('| {0:^20} | {1:^5} |'.format('NOMBRE', 'CANT.'))
            mostrar_jugadores_mayor_dato(lista_jugadores, key, dato_usuario, True)
            pause()
        else:
            print('NO HAY JUGADORES CON PROMEDIO MAYOR AL INGRESADO')
            pause()
    else:
        print('- Error - Ha ingresado un digito invalido...')
        pause()
