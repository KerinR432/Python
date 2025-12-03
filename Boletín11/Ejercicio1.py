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

class Pokemon:
    def __init__(self,codigo,nombre,evolucion = None):
        self.__codigo = codigo
        self.__nombre = nombre
        self._evolucion = evolucion
        self.__pv = random.randint(50,100)
    @property
    def codigo(self):
        return self.__codigo
    @property
    def nombre(self):
        return self.__nombre

    def validarCodigo(self):
        if self.__codigo >=1 and self.__codigo <= 151:
            return True
        return False

    def __str__(self):
        informe = f"""
        ╔═════════════════════════════╗
        ║        POKEDEX ENTRY        ║
        ╠═════════════════════════════╣
        ║ Código: {self.__codigo:<15}     ║
        ║ Nombre: {self.__nombre:<1} ║
        ║ Tipo: {self._evolucion:}      ║
        ║ vida: {self.__pv}           ║
        ╠═════════════════════════════╣
        ║ ¡Cuida mucho a tu compañero!║
        ╚═════════════════════════════╝
        """
        return informe

p3 = Pokemon(3,"Venasaur")
p2 = Pokemon(2,"Ivysaur",p3)
p1 = Pokemon(1,"Bulbasaur",p2)

print(p1.codigo)
print(p1.nombre)

print(p1)
print(p2)
print(p3)

