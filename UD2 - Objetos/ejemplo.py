#------------------------------------------------------
class CuentaCorriente:
    #* esto seria igual aun static, tiene el valor para todos los objetos
    __numCuentas = 0
    #* esto son funciones para crear constructores, se llaman funciones magicas.
    def __init__(self,codigo,titular,saldo=5000):
        #* Aqui metemos variables y metodos que queramos
        self.__codigo = codigo #* esto signfiica que es protegido "protected"
        self.__titular = titular
        self.__saldo = saldo #* y esto es privado "private"
        CuentaCorriente.__numCuentas+=1
#-------------------------------------------------
    #* como en java podemos hacer set y get una de las formas
#*segunda forma
    #?esto es un getter
    @property
    def saldo(self):
        return self.__saldo

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
#------------------------------------------------------
#* asi se llama las clases
c1 = CuentaCorriente(2343434,"Mohame",1000)
c2 = CuentaCorriente(2342432,"Freddy",5000)
c3 = CuentaCorriente(6567546,"Pepe",100)

#! no estan protegidos los datos,esto no ayuda mucho, pero esto ayudara a tener una buena practica
'''
c1.saldo = 56565
print(c1.saldo)
'''

print(c1.saldo)
print(CuentaCorriente.getNumCuenta())
c2.devolverDatoSucursal()
#----------------------------------------------------
#* el doble subrayado sera lo que mas vamos utilizar
#print(c1._titular) #* un subrayado de sirve de mucho
print(c1._CuentaCorriente__saldo) #* esto es la manera de Python para ocultar esos datos, pero se puede serguir manipulando

