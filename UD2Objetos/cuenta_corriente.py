#------------------------------------------------------
class CuentaCorriente:
    #* esto seria igual aun static, tiene el valor para todos los objetos
    __numCuentas = 0
    #* esto son funciones para crear constructores, se llaman funciones magicas.
    def __init__(self,codigo,titular,saldo=5000):
        #* Aqui metemos variables y metodos que queramos
        self.__codigo = codigo #* esto signfiica que es protegido "protected"
        self.__titular = []
        self.__titular.append(titular)
        self.__saldo = saldo #* y esto es privado "private"
        CuentaCorriente.__numCuentas+=1
#-------------------------------------------------
    #* como en java podemos hacer set y get una de las formas
#*segunda forma
    #?esto es un getter
    @property
    def saldo(self):
        return self.__saldo

    #?setter, importante siempre definirlo despues del getter
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
    # ! no se puede añadir un atributo que no viene especificado, tiene que devolver un String
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
c1 = CuentaCorriente(2343434,"Mohame",1000)
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
#! no estan protegidos los datos,esto no ayuda mucho, pero esto ayudara a tener una buena practica
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
#* el doble subrayado sera lo que mas vamos utilizar
#print(c1._titular) #* un subrayado de sirve de mucho
print(c1._CuentaCorriente__saldo) #* esto es la manera de Python para ocultar esos datos, pero se puede serguir manipulando

#* aqui se muestra, puede ser el toString en JAVA
print(str(c1))
print(str(c2))
print(str(c3))
#* otra manera
print(c1)
#----------------------------------------------------
#* clase sin funcionalidad vacia
class Alumno:
    pass

Alumno1 = Alumno()
Alumno1.nombre="Juan"
Alumno1.apellido="Balas"
Alumno1.edad=24
Alumno1.telefono=65555232

#----------------------------------------------------
#*Metodos magicos ocmo metodos dunder
"""
__init__ consctructor 
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