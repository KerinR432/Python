#* clase padre
class Padre:
    def __init__(self):
        self._titulo = "soy la clase padre"

    def mostrar(self):
        print("ppp",self._titulo)


class Madre:
    def __init__(self):
        self._titulo = "soy la madre"

    def mostrar(self):
        print("mmm",self._titulo)

#* HERENCIA MULTIPLE, va dar preferencia a lo de la izquierda.Pero hay otra forma de dar preferencia
class hijo(Padre,Madre):

    def __init__(self):
        self._titulo = "Soy la clase hijo" #_hijo_titulo

    #* Con super llamas a la clase padre, herenandola, se puede llamar enconcreto a cualquier padre
    def mostrar(self,mensaje):
        Padre.mostrar(self)
        #super().mostrar()
        print(mensaje)
objecto1 = Padre()
objecto1.mostrar()
objecto2 = Madre()
objecto2.mostrar()

objecto3 = hijo()
objecto3.mostrar("Mensaje extra")
