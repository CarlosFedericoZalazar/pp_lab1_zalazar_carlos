import re

dict_jugador = {"logros": [
        "3 veces campeón de la NBA",
        "2 veces MVP de la NBA",
        "12 veces All-Star",
        "Miembro del Salon de la Fama del Baloncesto"
      ]
}

def validacion_fama(texto):
    patron = r'\bfama\b|\bFama\b'
    if bool(re.search(patron,texto)):
        print('la pegaste man')
    else:
        print('mandaste cualquiera')

texto = 'Miembro del Salon de la fama del Baloncesto'
validacion_fama(texto)