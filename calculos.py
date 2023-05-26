def calcular_promedio_puntos_partido(lista_jugadores):
    aucumulador_puntos = 0
    for jugador in lista_jugadores:
        aucumulador_puntos += jugador['estadisticas']['promedio_puntos_por_partido']
    promedio_puntos = aucumulador_puntos / len(lista_jugadores)
    print('\nEl promedio total de puntos por partido del equipo es: {0:.2f}\n'.format(promedio_puntos))
