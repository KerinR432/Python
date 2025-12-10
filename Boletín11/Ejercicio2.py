"""
2. Queremos implementar una clase para gestionar nuestra colección de mangas con las
siguientes características:

- Por cada manga guardaremos el nombre del mangaka (autor) el título de la colección (en
japonés, obligatorio y en español, opcional), el género prinicpal (shonen, shojo, seinen, josei,
kodomo, yuri, spokon, isekai y hentai) y el último número publicado en la colección. Crea
getters para todos ellos y setter para el título en castellano (por si originalmente no lo
sabemos y luego lo queremos añadir) y para el número por el que va la colección.

- Queremos, además, poder actualizar los números que tenemos y saber que números nos
faltan. Para ello crearemos dos métodos: uno que nos permitirá introducir los números que
vamos comprando (permitiendo una entrada variable de argumentos para cuando
compramos mas de uno a la vez) y otro que nos diga que números nos faltan para completar
la colección.

- Si cuando introducimos los números que compramos resulta que ya tenemos alguno de
ellos repetido debería de advertirnos.

- También necesitaremos un método que nos permita eliminar un número (lo hemos perdido,
etc.). Si tratamos de eliminar un número que no tenemos debería de advertírsenos
"""
class ColecionMangas():
    genero = {"Shone","Shojo","Seinen","Josei","Kodomo","Yuri","Spokon","Isekai","Hentai"}
    def __init__(self,autor,titulo):