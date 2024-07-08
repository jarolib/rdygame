import random
from menus import opciones, menu_inventario
from personaje import Jugador, Enemigo
from objetos import loot

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

def combate(j1, enemy):
    while j1.get_vida() > 0 and enemy.get_vida() > 0:
        opc = ["Uir", "Atacar", "Usar Objeto"]
        eleccion = opciones(opc)
        if eleccion == 0:
            j1.uir()
            break
        elif eleccion == 1:
            enemy.recibir_daño(j1.atacar())
            print(j1._nombre, "ha atacado")
            print(j1._nombre, "tiene", j1._vida, "de vida.")
            print(enemy._nombre, "tiene", enemy._vida, "de vida.")
        elif eleccion == 2:
            opc = j1.get_inventario()
            j1.usar_objeto(menu_inventario(j1.get_inventario()))        
        if enemy.get_vida() <= 0:
            print("Enemigo pierde")
            break
        j1.recibir_daño(enemy.atacar())
        print(enemy._nombre, "ha atacado")
        print(j1._nombre, "tiene", j1._vida, "de vida.")
        print(enemy._nombre, "tiene", enemy._vida, "de vida.")
        if j1.get_vida() <= 0:
            print("Jugador Pierde")

def cofre():
    obj = random.choice(loot)
    print("Dentro del cofre hay", obj)
    return obj
    