"""
1. Crea una función en python que se llame compararFicheros y que reciba como argumento el
nombre de dos ficheros de texto. La función debería de devolver un valor booleano indicando
si el contenido de ambos ficheros es exactamente el mismo o no.

"""

def comprarFichero():
    try:
        fichero1 = open("fichero1","r")
        textoFichero1 = fichero1.read()
        fichero1.close()
        fichero2 = open("fichero2","r")
        textoFichero2 = fichero2.read()
        fichero2.close()
        if textoFichero1 == textoFichero2:
            return True
        else:
            return False
    except:
        print("Fichero comparado y no es exactamente")

if comprarFichero()==False:
    print("fichero es distinto")
else:
    print("Fichero comparado y es igual")