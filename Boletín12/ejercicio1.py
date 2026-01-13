"""
1. Queremos implementar una clase para gestionar una aplicación de gestión de notas. Cada
nota tendrá cuatro elementos: título, descripción, color (debe de se amarillo, verde, blanco o
cyan para una futura implementación en un entorno gráfico) y fecha de creación.
Necesitamos, además, añadir los siguientes métodos: crearNota, eliminarNota y listarNota
No hace falta que hagas entradas por teclado: crea los métodos y pruébalos llamándolos
directamente.
Trata de que la visualización de la nota sea lo mas agradable posible en pantalla usando
fstrings
"""

class Nota:

    def __init__(self,titulo,descripcion,fecha_creacion):
        self._titulo = titulo
        self._descripcion = descripcion
        self._fecha_creacion = fecha_creacion

    def crearNota(self,titulo,descripcion,fecha_creacion):
        self._titulo = titulo
        self._descripcion = descripcion
        self._fecha_creacion = fecha_creacion

    def eliminarNota(self):
        self._titulo = None
        self._descripcion = None
        self._fecha_creacion = None

    def listarNota(self):
        print(f"""
        📌 Título: {self._titulo}
        📝 Descripción: {self._descripcion}
        📅 Fecha: {self._fecha_creacion}
        """)


N1 = Nota("pepito","Dinero o algo asi","12-12-12")
print(N1.listarNota())
N1.eliminarNota()
print(N1.listarNota())