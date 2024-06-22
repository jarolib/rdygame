from objetos import basicos, armas
from abc import ABC, abstractmethod

class Personaje(ABC):
    @abstractmethod
    def __init__(self, nombre, clase) -> None:
        self._nombre = nombre
        self._clase = clase
        self._vida = 100
        self._aguante = 100
        self._escudo = 0

        if clase == "Humano":
            self._fuerza = 25
            self._magia = 5
        elif clase == "Guerrero":
            self._fuerza = 30
            self._magia = 0
        elif clase == "Mago":
            self._fuerza = 5
            self._magia = 25
        elif clase == "Paladin":
            self._fuerza = 15
            self._magia = 15

    
    @abstractmethod
    def ver_vida(self):
        pass
    
    @abstractmethod
    def ver_inventario(self):
        pass
    
    @abstractmethod
    def usar_objeto(self, obj):
        pass

class Jugador(Personaje):
    def __init__(self, nombre, clase) -> None:
        super().__init__(nombre, clase)

        self._inventario = [["PocionVida", 3], 
                            ["PocionAguante", 1],
                            ["Rodela", 1]]

    def __limpiar_inventario(self):
        auxlist = []
        for i in range(len(self._inventario)):
            if self._inventario[i][1] > 0:
                auxlist.append(self._inventario[i])
        self._inventario = auxlist

    def get_fuerza(self):
        return self._fuerza
    
    def get_magia(self):
        return self._magia
    
    def get_escudo(self):
        return self._escudo
    
    def get_vida(self):
        return True if self._vida > 0 else False


    def ver_jugador(self):
        print(f"Nombre: {self._nombre}")
        print(f"Clase: {self._clase}")
        print(f"Vida: {self._vida}")
        print(f"Aguante: {self._aguante}")
        print(f"Escudo: {self._escudo}")
        print(f"Fuerza: {self._fuerza}")
        print(f"Magia: {self._magia}")
        self.ver_inventario()


    def ver_vida(self):
        print(self._vida)
    
    def ver_inventario(self):
        for i in range(len(self._inventario)):
            print(self._inventario[i][0], "x", self._inventario[i][1])
    
    def usar_objeto(self, obj):
        for i in range(len(self._inventario)):
            if obj in self._inventario[i][0] and self._inventario[i][1] > 0:
                if obj in basicos:
                    self._vida += basicos[obj][0]
                    self._aguante += basicos[obj][1]
                    self._fuerza += basicos[obj][2]
                    self._magia += basicos[obj][3]
                    
                elif obj in armas:
                    self._fuerza += armas[obj][0]
                    self._escudo += armas[obj][1]
                    self._magia += armas[obj][2]
                    
                self._inventario[i][1] -= 1       
        self.__limpiar_inventario()
    
    def uir(self):
        if self._aguante > 24:
            self._aguante -= 25
        else: 
            print("No tienes aguante suficiente para uir")
    
    def recibir_daño(self, otro):
        if self._escudo >= otro:
            self._escudo -= otro
        else:
            rotura = otro - self._escudo
            self._escudo = 0
            self._vida -= rotura

class Enemigo(Personaje):
    def __init__(self, nombre, clase) -> None:
        super().__init__(nombre, clase)

        self.ver_inventario = []

    def __limpiar_inventario(self):
        auxlist = []
        for i in range(len(self._inventario)):
            if self._inventario[i][1] > 0:
                auxlist.append(self._inventario[i])
        self._inventario = auxlist

    def get_fuerza(self):
        return self._fuerza
    
    def get_magia(self):
        return self._magia
    
    def get_escudo(self):
        return self._escudo
    
    def get_vida(self):
        return True if self._vida > 0 else False


    def ver_jugador(self):
        print(f"Nombre: {self._nombre}")
        print(f"Clase: {self._clase}")
        print(f"Vida: {self._vida}")
        print(f"Aguante: {self._aguante}")
        print(f"Escudo: {self._escudo}")
        print(f"Fuerza: {self._fuerza}")
        print(f"Magia: {self._magia}")
        self.ver_inventario()


    def ver_vida(self):
        print(self._vida)
    
    def ver_inventario(self):
        for i in range(len(self._inventario)):
            print(self._inventario[i][0], "x", self._inventario[i][1])
    
    def usar_objeto(self, obj):
        for i in range(len(self._inventario)):
            if obj in self._inventario[i][0] and self._inventario[i][1] > 0:
                if obj in basicos:
                    self._vida += basicos[obj][0]
                    self._aguante += basicos[obj][1]
                    self._fuerza += basicos[obj][2]
                    self._magia += basicos[obj][3]
                    
                elif obj in armas:
                    self._fuerza += armas[obj][0]
                    self._escudo += armas[obj][1]
                    self._magia += armas[obj][2]
                    
                self._inventario[i][1] -= 1      
        self.__limpiar_inventario()          

        

