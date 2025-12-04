"""
profesores = ["Jose Maria", "Natalia", "Aguistin"]
Iterador = iter(profesores)
print(next(Iterador))
print(next(Iterador))
print(next(Iterador))
print(next(Iterador, "STOP"))

"""

class DiasDeLaSemana:
    def __init__(self, dia):
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Sábados", "Domingo"]
        self.dia = dia

    def __iter__(self):
        return self

    def __next__(self,stop=None):
        if self.dia == 6:
            self.dia = 0
        dia_actual = self.dias[self.dia]
        if dia_actual == 'domingo':
            dia_actual = 'Lunes'
            self.dia = 1
        self.dia+=1
        return dia_actual


semana = DiasDeLaSemana(1)
iterador = iter(semana)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador,"Adios"))
