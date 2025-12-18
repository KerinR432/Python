class Tarea:
    listado = {}
    def __init__(self,id,titulo,prioridad):
        self.__id = id
        self.__titulo = titulo
        self.__prioridad = prioridad
        self.__completado = False
        comprobarTareas(self)

    def comprobarTareas(self):
        if self.listado["id"] = self.__id:
            print("Error")
        else:
            Tarea.listado[self.__id] = self

t1 = Tarea("T1  ","Aprender Python",10)