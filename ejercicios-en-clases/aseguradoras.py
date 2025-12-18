from abc import ABCMeta

from UD2Objetos.pkmAbstracta import Abstracta


class Vehiculo(metaclass=ABCMeta):
    def __init__(self,matricula,año_venta):
        self.__matricula = matricula
        self.__año_venta = año_venta

    #Getters
    @property
    def matricula(self):
        return self.__matricula
    @property
    def año_venta(self):
        return self.__año_venta

    #setters
    @matricula.setter
    def matricula(self,matricula):
        self.__matricula = matricula
    @año_venta.setter
    def año_venta(self,año_venta):
        self.__año_venta = año_venta

    @abstractmethod
    def subidaDe

class Coche(Vehiculo):
    def __init__(self):

