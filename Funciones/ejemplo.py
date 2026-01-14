def miFuncion (): #* se crean funciones
    print("Hola soy una función")

miFuncion()

def funcionConParametro(mensaje): #* se crea una función con parametro
    valor = 5
    print(mensaje,valor) #* existe un ambito dentro de la funciones, tiene variables distinta

funcionConParametro("Hola Mundo")

def valorRetorno(nombre,despedida):
    return "Hola " + nombre + despedida #*devolver con un return
sucursalMadrid
nombre = "José María"
print(valorRetorno(nombre, " Que te vaya bien"))


def devolveNumeros():
    return 1,2,3 #* devolver mas de algun return

n1,n2,n3 = devolveNumeros()
print(n1,n2,n3, sep="-")

def funcion(valor):
    valor*=5
    print(valor)

n = 2
funcion(n) #*manda una copia
print(n) #*muestra la copia original

def funcion2(valor):
    valor[0]*=5
    print(valor)

n = [2]
funcion2(n) #* con las listas si pasa
print(n)

def valorRetorno2(nombre,despedida = " te veo pronto!"):
    return "Hola " + nombre + despedida

nombre = "José María"
print(valorRetorno2(nombre, " Que te vaya bien"))
print(valorRetorno2("Antonio")) #* coje el valor por defecto

def muestraProfe(*nombres): #*Meter un numero de varible posible

    print(nombres)

muestraProfe("Natalia","Agustín")
muestraProfe("Pedro","José María","Ana","Puche")

def repitreNombre(veces,nombre):
    for _ in range(veces):
        print(nombre,end=" *** ")

datos = [2,"pepe"]
datos2 = [4,"Luis"]
repitreNombre(*datos)
repitreNombre(*datos2)
repitreNombre(*[3,"eva"])

def prueba(arg1:int,arg2:float) -> str:#*aun con 2 argumento devuelve lo que sea, pero esto es como un comentario
    #*ayuda a ver como programador
    return "Hola"
