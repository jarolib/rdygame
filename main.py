from personaje import Personaje, Jugador, Enemigo
from menus import opciones, menu_inventario, creacion_personaje
from tools import combate, cofre

j1 = creacion_personaje()
jugador = Jugador(j1[0], j1[1])
jugador.ver_inventario()
jugador.actualizar_inventario(cofre())
jugador.ver_inventario()
jugador.actualizar_inventario(cofre())
jugador.actualizar_inventario(cofre())
jugador.actualizar_inventario(cofre())
jugador.ver_inventario()


