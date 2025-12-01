"""
1. Queremos implementar una clase para gestionar un juego de Pokemon con las siguientes
características:
- Los atributos base que manejaremos serán código, nombre y tipo
- Sólo trabajaremos con pokemon de primera generación por lo que el código estará entre el
1 y el 151, ambos incluidos- Los posibles tipos son Normal, Agua, Fuego, Planta, Volador, Lucha, Veneno, Eléctrico,
Tierra, Roca, Psíquico, Hielo, Bicho, Fantasma y Dragón.
- Cada pokemon debe de ser de un tipo pero podría ser de dos. Nunca mas
- No necesitamos setters (ya que un pokemon una vez creado no puede modificar sus
características) pero si getters apropiados para todas ellas
- Además, crearemos un método que se llame evolución que permitirá que un pokemon
evolucione en otro diferente. Para ello si un pokemon puede evolucionar en otro debe de
tener de alguna forma una referencia al pokemon en el que evoluciona.
"""
class Pokemon:
    __codigo = 0
    __nombre = ""
    __tipo = ""

    def __init__(self,codigo,nombre,tipo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__tipo = tipo
    @property
    def codigo(self):
        return self.__codigo
    @property
    def nombre(self):
        return self.__nombre
    @property
    def tipo(self):
        return self.__tipo

    def __str__(self):
        informe = f"""
        ╔═════════════════════════════╗
        ║        POKEDEX ENTRY        ║
        ╠═════════════════════════════╣
        ║ Código: {self.__codigo:<15} ║
        ║ Nombre: {self.__nombre:<14} ║
        ║ Tipo: {self.__tipo:<16}     ║
        ╠═════════════════════════════╣
        ║ ¡Cuida mucho a tu compañero!║
        ╚═════════════════════════════╝
        """
        print(informe)

p1 = Pokemon(1,"Pikachu","Electrico")

print(p1.codigo)
print(p1.nombre)
print(p1.tipo)

print(str(p1))