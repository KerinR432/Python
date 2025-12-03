"""
1. Queremos implementar una clase para gestionar un juego de Pokemon con las siguientes
características:
- Los atributos base que manejaremos serán código, nombre y tipo
- Sólo trabajaremos con pokemon de primera generación por lo que el código estará entre el
1 y el 151, ambos incluidos
- Los posibles tipos son Normal, Agua, Fuego, Planta, Volador, Lucha, Veneno, Eléctrico,
Tierra, Roca, Psíquico, Hielo, Bicho, Fantasma y Dragón.
- Cada pokemon debe de ser de un tipo pero podría ser de dos. Nunca mas
- No necesitamos setters (ya que un pokemon una vez creado no puede modificar sus
características) pero si getters apropiados para todas ellas
- Además, crearemos un método que se llame evolución que permitirá que un pokemon
evolucione en otro diferente. Para ello si un pokemon puede evolucionar en otro debe de
tener de alguna forma una referencia al pokemon en el que evoluciona.
"""
import random
from xmlrpc.client import FastParser


class Pokemon:
    def __init__(self, codigo, nombre, evolucion=None):
        self.__codigo = codigo
        self.__nombre = nombre
        self._evolucion = evolucion
        self.__pv = random.randint(50, 100)

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    def evoluciona(self):
        if self._evolucion is None:
            evo = self
            print("Este pokemon no tiene mas evoluciones")
            # return self
        else:
            evo = self._evolucion
            # return self._evolucion
        return evo

    def sigueVivo(self,p1,p2):
        puedeCombatir = True
        if p1 == 0 or p2 == 0:
            puedeCombatir = False
        if p1 == 0 and p2 == 0:
            puedeCombatir = False

        return puedeCombatir



    def combatePokemon(self,contricante):

      if self.sigueVivo(self.__pv,contricante.__pv) == True:
            ataque = random.randint(25,75)
            if contricante.__pv<ataque:
                print(f"{contricante.__nombre} ha sido Noqueado 😵")
            else:
                ataque = random.randint(25, 75)
                self.__pv -= ataque
                if self.__pv <=0:
                    print(f"{self.__nombre},ha sido derrotado ")
                else:
                    print(f"Ninguno de los pokemons no ha sido derrotado")
      else:
          print("No se puede luchar, El pokemon ha sido derrotado")
    def MotrarPokemon(self):
        informe = f"""
        ╔═════════════════════════════╗
        ║        POKEDEX ENTRY        ║
        ╠═════════════════════════════╣
        ║ Código: {self.__codigo:<19} ║
        ║ Nombre: {self.__nombre:<19} ║
        ║ evolucion: {self.evoluciona().__nombre:<11}      ║
        ║ vida: {self.__pv:<15}       ║
        ╠═════════════════════════════╣
        ║ ¡Cuida mucho a tu compañero!║
        ╚═════════════════════════════╝
        """
        print(informe)


p3 = Pokemon(3, "Venasaur")
p2 = Pokemon(2, "Ivysaur", p3)
p1 = Pokemon(1, "Bulbasaur", p2)
p1.MotrarPokemon()
p2.MotrarPokemon()
p3.MotrarPokemon()
p1 = p1.evoluciona()
p3 = p3.evoluciona()

print("-------------------")
p1.MotrarPokemon()
p3.MotrarPokemon()

print("-------------------")
p1.combatePokemon(p3)
p1.MotrarPokemon()
p3.MotrarPokemon()

print("----------------------")
p1.combatePokemon(p3)