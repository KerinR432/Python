from abc import abstractmethod, ABCMeta

#* clase abstracta
class Abstracta(metaclass=ABCMeta):
    def metodoNormal(self):
        print("Hola mundo")

    @abstractmethod #* tiene que llevar siempre este decoración
    def metodoAbstracto(self):
        pass

class hija(Abstracta):
    def metodoAbstracto(self):
        print("Adios")


elemento = hija()
elemento.metodoNormal()
elemento.metodoAbstracto()