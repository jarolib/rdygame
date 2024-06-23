def opciones(lista_opciones):
    print("Elige una opción:")
    print("-----------------")
    for i in range(len(lista_opciones)):
        print(i, lista_opciones[i])
    eleccion = int(input("¿Qué quieres hacer?: "))
    print("Has elegido", lista_opciones[eleccion])
    return eleccion

def menu_inventario(list_inventario):
    print("Elige un objeto para usar:")
    print("--------------------------")
    for i in range(len(list_inventario)):
        print(i, list_inventario[i][0], "x", list_inventario[i][1])
    eleccion = int(input("¿Qué objeto quieres usar? "))
    print("Has usado", list_inventario[eleccion][0])
    return list_inventario[eleccion][0]
