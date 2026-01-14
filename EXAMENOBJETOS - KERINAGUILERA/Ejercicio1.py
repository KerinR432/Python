import re
patron = r"[0-9]{4}"
class Sucursales:
    def __init__(self,direccion,provincia,codigo):
        self.__direccion=direccion
        self.__provincia=provincia
        if re.fullmatch(patron,codigo):
            self.__codigo=codigo

    def __str__(self):
        return f"""
                EL BANCO DE LA PROVIANCIA DE: {self.__provincia}
                EN LA CALLE: {self.__direccion}
                CON EL CODIGO: {self.__codigo}
                """
    def codigo(self):
        return self.__codigo

    def provincia(self):
        return self.__provincia



class Cliente:
    def __init__(self,nombre,apellido,nif,telefono,Sucursales):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__nif=nif
        self.__telefono=telefono
        self.__Sucursales=[]
    def nombre(self):
        return self.__nombre


class CuentaCorriente:
    def __init__(self,codigo,saldo,Sucursales,Cliente):
        self.__codigo=[codigo]
        self.__saldo=saldo
        self.Cliente=Cliente
        self.Sucursales=Sucursales
    def codigoIBAN(self):
        for i in range(0, len(self.__codigo)):
            codigo = self.__codigo[i]
            IBANS = (f"ES68 1234 {self.Sucursales.codigo()} {self.__codigo[i]}")
        return IBANS
    def mostrarIBAN(self,nombre):
        if nombre == self.Cliente.nombre():
            return f"""
                    {self.Cliente.nombre()}. Cliente de la sucursal {self.Sucursales.codigo()} ({self.Sucursales.provincia()})
                    {f"ES68 1234 {self.Sucursales.codigo()} {self.codigoIBAN()} - {self.__saldo}€"}
                    Saldo total: {self.__saldo}€
                    """
#LUGAR DE PRUEBAS

sucursalMadrid = Sucursales("Calle villa alto 8","Madrid", "0012")
Mohame = Cliente("Mohame","Salami","A321312312","60421231",sucursalMadrid)
freddy = Cliente("Freddy","Andrade","F1313231","121312312",sucursalMadrid)
print("Entidad Bancaria")
cuentaCorrienteDeMoha = CuentaCorriente("021313103",1500,sucursalMadrid,Mohame)
cuentaCorrienteDeMoha2 = CuentaCorriente("021313123123",1700,sucursalMadrid,Mohame)
print(cuentaCorrienteDeMoha.mostrarIBAN("Mohame"))