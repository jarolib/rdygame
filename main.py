from personaje import Personaje, Jugador, Enemigo
from menus import opciones, menu_inventario
from tools import combate

jugardor = Jugador("Roldy", "Paladin")
enemigo = Enemigo("Eva", "Humano")

combate(jugardor, enemigo)