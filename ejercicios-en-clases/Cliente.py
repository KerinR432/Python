class cliente:
    def __init__(self,nombre,nif,año_nacimiento,año_sacar_carnet,puntos_carnet,Vehiculo):
        self.__nombre = nombre
        self.__nif = nif
        self.__año_nacimiento = año_nacimiento
        self.__año_sacar_carnet = año_sacar_carnet
        self.__puntos_carnet = puntos_carnet
        self.__Vehiculo = [Vehiculo]
    @property
    def nombre(self):
        return self.__nombre
    @property
    def nif(self):
        return self.__nif
    @property
    def año_nacimiento(self):
        return self.__año_nacimiento
    @property
    def año_sacar_carnet(self):
        return self.__año_sacar_carnet
    @property
    def puntos_carnet(self):
        return self.__puntos_carnet
    @property
    def Vehiculo(self):
        return self.__Vehiculo

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    @nif.setter
    def nif(self,nif):
        self.__nif = nif
    @año_nacimiento.setter
    def año_nacimiento(self,año_nacimiento):
        self.__año_nacimiento = año_nacimiento
    @año_sacar_carnet.setter
    def año_sacar_carnet (self,año_sacar_carnet):
        self.__año_sacar_carnet = año_sacar_carnet
    @puntos_carnet.setter
    def puntos_carnet(self,puntos_carnet):
        self.__puntos_carnet = puntos_carnet
    @Vehiculo.setter
    def Vehiculo(self,Vehiculo):
        self.__Vehiculo = Vehiculo
    