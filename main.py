from archivos import *
from funciones import *

lista_dt = leer_json('dt.json')
if lista_dt:
    inicio_app_dt(lista_dt)
else:
    print('Error al intentar leer el archivo')

