class CuentaCorriente:
    #manera de hacer statics para todos los obj
    __numCuentas=0  # atributo "static"

    #self es para el objeto
    def __init__(self,codigo,titular,saldo=5000):    #es un metodo magico
        self._codigo=codigo  # atributo "protegido"
        self.__titular=titular  # atributo "privado"
        self.saldo=saldo  # atributo "publico"
        #para llamar al statico
        CuentaCorriente.__numCuentas+=1

    @classmethod    #metodo de la clase
    def getNumCuentas(cls):
        return cls.__numCuentas

    @staticmethod   #metodo estático
    def getDatosSucursal():
        return "Calle del Pez, 7. 28032. Madrid"

    @property
    def saldo(self):
        return self.saldo
    @saldo.setter   #setter, siempre después del property
    def saldo(self,saldo):
        self.saldo=saldo


    @property   #Este metodo actúa como atributo/propiedad
    def titular(self):
        return self.__titular

c1=CuentaCorriente(2420,"Jose",1000)
c2=CuentaCorriente(2421,"maria")
print(c1.getDatosSucursal())

#registro, es una clase vacia
class Alumnos:
    pass

#aqui le pasamos los atributos
alumno1=Alumnos()
alumno1.nombre="Juan"
alumno1.edad=25
alumno1.apellidos="Perez"