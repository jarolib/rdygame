import random

def nombre_aleatorio(lon):
    vocales = "aeiou"
    abecedario = "bcdfghjklmnpqrstvwxyz"
    nombre = random.choice(vocales + abecedario)
    for i in range(lon-1):
        if nombre[i] in vocales:
            nombre += random.choice(abecedario)
        else:
            nombre += random.choice(vocales)
    return nombre.capitalize()