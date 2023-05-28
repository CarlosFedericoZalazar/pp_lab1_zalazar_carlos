import json

def leer_json(path:str):
    """ carga el archivo JSON
    Args:
        path (str): ruta del archivo"""
    
    with open(path, 'r', encoding="utf-8") as file:
        lista = json.load(file)
    return lista

def guardar_archivo_csv(nombre:str,data:str):
    """ genera un archivo csv"""
    with open('estadisticas\\'+nombre, 'w') as file:
        file.write(data)