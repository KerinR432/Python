#------------------------------------------------------
class CuentaCorriente:
    #* esto sería igual aún static, tiene el valor para todos los objetos
    __numCuentas = 0
    #* esto son funciones para crear constructores, se llaman funciones mágicas.
    def __init__(self,codigo,titular,saldo=5000):
        #* Aquí metemos variables y metodos que queramos
        self.__codigo = codigo #* esto significa que es protegido "protected"
        self.__titular = []
        self.__titular.append(titular)
        self.__saldo = saldo #* y esto es privado "prívate"
        CuentaCorriente.__numCuentas+=1
#-------------------------------------------------
    #* como en java podemos hacer set y get una de las formas
#*segunda forma
    #? Esto es un getter
    @property
    def saldo(self):
        return self.__saldo

    #? Setter, importante siempre definirlo después del getter
    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo
    """
        def setSaldo(self,saldo):
            self.__saldo = saldo

        def getSaldo(self):
            return self.__saldo

    """

    #----------------------------------
    #* decorador de clases, cls llama a la misma clase, simboliza esa misma clase
    @classmethod
    def getNumCuenta(cls):
        return (cls.__numCuentas)
    #* no manipula nada de los datos, sino llamar
    @staticmethod
    def devolverDatoSucursal():
        print("Calle del Pez, 7. 28032. Madrid")
    #-------------------------------------------------
    # !No se puede añadir un atributo que no viene especificado, tiene que devolver un String
    # * puede ser el toString de JAVA
    def __str__(self):
        documento = f"""
                    |---------------------|
                     el codigo: {self.__codigo}
                     el titular es: {self.__titular}
                     y tu saldo es: {self.__saldo}€
                    |---------------------|
                    """
        return documento

    def __add__(self, segundaCuenta):
        self.__saldo+=segundaCuenta.__saldo
        self.__titular += segundaCuenta.__titular

        return self

#------------------------------------------------------
#* asi se llama las clases
c1 = CuentaCorriente(2343434,"Mohamed",1000)
c2 = CuentaCorriente(2342432,"Freddy",5000)
c3 = CuentaCorriente(6567546,"Pepe",100)

#--------------------------------------------------------
#*sobre cargar de funciones
def funcionSobreCargada(valor):
    if isinstance(valor, int):
        print("Estoy recibiendo un entero")
    elif isinstance(valor, str):
        print("estoy recibiendo un estring")
    else:
        print("Estoy recibiendo otra cosa y no se que hace ella...")

funcionSobreCargada(5)
funcionSobreCargada("HOLA")
funcionSobreCargada(5)
#----------------------------------------------------------
#! No están protegidos los datos, esto no ayuda mucho, pero esto ayudará a tener una buena práctica
'''
c1.saldo = 56565
print(c1.saldo)
'''
c1.saldo = 5870
print(c1.saldo)
print(CuentaCorriente.getNumCuenta())
c2.devolverDatoSucursal()

#* sumas los objetos
c1 = c1 + c2
print(str(c1))
#----------------------------------------------------
#* el doble subrayado será lo que más vamos utilizar
#print(c1._titular) #* un subrayado te sirve de mucho
print(c1._CuentaCorriente__saldo) #* esto es la manera de Python para ocultar esos datos, pero se puede seguir manipulando

#* aquí se muestra, puede ser el toString en JAVA
print(str(c1))
print(str(c2))
print(str(c3))
#* otra manera
print(c1)
#----------------------------------------------------
#* clase sin funcionalidad vacía
class Alumno:
    pass

Alumno1 = Alumno()
Alumno1.nombre="Juan"
Alumno1.apellido="Balas"
Alumno1.edad=24
Alumno1.telefono=65555232

#----------------------------------------------------
#*Metodos mágicos como metodos dunder
"""
__init__ constructor 
__del__ el destructor de objeto
__str__ del vuelve texto
__len__ mide la longitud de un objeto
__add__
__sub__
__mul__
__truediv__
__eq__ igual
__ne__ no igual
__gt__ 
__lt__
crear nuestro propios
__iter__
__next__
"""