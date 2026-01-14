class Biblioteca:

    def __init__(self,Libro,Comic):
        self.Libro = Libro
        self.Comic = Comic
        self.colecion = {}
    def añadirABiblioteca(self):
        self.colecion[self.Libro.codigo] = self.Libro
class Libro:

    def __init__(self,codigo,numeroPagina,titulo,autor,edicion,numeroEjemplares):
        self.codigo = codigo
        self.numeroPagina = numeroPagina
        self.titulo = titulo
        self.autor = autor
        self.edicion = edicion
        self.numeroEjemplares = numeroEjemplares


class Comic:
    def __init__(self,codigo,numeroPagina,titulo,autor,color):
        self.codigo = codigo
        self.numeroPagina = numeroPagina
        self.titulo = titulo
        self.autor = autor
        self.color = color


WillEisner = Libro("001",150,"Viaje al corazón de la tormenta","Will Eisner","12",5)

biblioteca1 = Biblioteca(WillEisner)
biblioteca1.añadirABiblioteca(WillEisner)