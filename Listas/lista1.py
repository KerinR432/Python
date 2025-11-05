import random
#Dos formas de crear listas variable no tipada
lista = [] #una lista vacía
lista2 = list()
#Inicializar una lista con elementos
lista3 = [2,4,589,33,1,44,6,7,2] # pueden existir elemento repito, dependiendo de la posición
lista4 = ["Eva","alvaro","Sara"] #Lista de String
lista5 = [34,"Jose Maria",False,45.6,2,"Perez",[1,5,"DAM"]] #son estructura heterogénea, que cada elemento de la lista puede ser lo que da la ganan
# puede existir lista dentro de las listas
#recorrrer una lista
for i in lista5:
    print(i)
for i in range(0,len(lista5)): # otra manera de recorrer
    print(i,"-", lista5[i]) # podemos mostrar la posición de los datos de la lista

print(lista5[6][2]) #buscar una variable de una lista dentro otra lista
print("\n🔥Matriz🔥\n")
matriz = [[1,2,3],[4,5,6],[7,8,9]]#vector de 2 dimensiones
print(matriz[2][0])

#podemos sumar listas de dos formas "+" o un método
print("\nsuma con el '+'💫\n")
lista6 = lista3 + lista4
print(lista6)
print("\nsuma con método🤑\n")
lista3.extend(lista4) #otra manera de sumar con método pero pierdes la lista 3😨
print(lista3)
print("\nInsertar datos\n")
#Añadir elemento en lista dependiendo de la posición
lista7 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista7)
lista7.insert(1,333) #se mete antes de la posición que le mandemos y si metemos cualquier numero que no este en la lista lo mete al final
print(lista7)
#eliminar
print("\nEliminar\n")
elemento = lista7.pop(2)#eliminas el último elemento y lo recuperas y si le ponemos (n) recupera esa posción de la memoria
# Y si ponemos (-n) empieza de tras hacia delante
print(elemento)
print(lista7)
lista7.remove(3)#elimina una elemento en concreto
print(lista7)

#Ordenar una lista
print("\nOrdenar\n")
lista7 = [111,22,333,4,55,6.5,7,1234,3]#decimales se pueden ordenar, texto y número no se puede
lista7.sort()#sort ordena de manera accented y numéricamente y alfabéticamente sería como lo haría a los ordenadores
print(lista7)
#lista7.sort(reverse=True)#reverse ordena de manera descendente
print(lista7)
#buscar un elemento
print("\nBuscar elementos🔍\n")
if 333 not in lista7: #la manera sencilla de buscar un elemento solo saber si esta
    print("No esta en la lista😔")
else:
    print("esta en la lista🎊")
    print(f"aparece {lista7.count(333)} veces")#para contar cuantas veces aparece en la lista y si el elemento no está en la lista devuelve 0

if 0 in lista:
    print(lista7.index(0))#devuelve la primera posción de donde aparece y devuelve una excepción si falta
print("\n conversión\n")
texto = "Hola Mundo"
lista7 = list(texto)#puedes transformar un elemento texto en una lista y que cada caracter sea un elemento de la lista
print(lista7)
lista7 = [1,2,3,4,5,6,7,8]
texto2 = str(lista7)#convierte una lista en texto
print(texto2)
texto2= texto2.replace("["," ")#poder quitar la última coma y dejarlo bonito, guárdate esto
texto2= texto2.replace("]"," ")
print(texto2)
vector = str(matriz[1])
print(vector)

lista7 = [1,2,3,4,5,6,7,8]
print(lista7[::-1])#también se puede hacer un bocadillo🥪 y si pongo un paso ':' y es 2 cogería los impares de la lista
# Y él -1 es para ir de al reves en la lista.
#Interacturar con RANDOM
print("\nRandom🔃\n")

alumnos = ["Alvaro","Sara","Eva","Fernando","Juan"]
print(random.choice(alumnos))#extrae un elemento random de un a lista
print(random.sample(alumnos,4))#sample extrae tanto elemento que queramos sin querer repeticiones
random.shuffle(alumnos)#desordena la lista original
print(alumnos)

listaNombre = ["Ana","Verónica","Luis","Rafael"]
for nombre in listaNombre:#* Si no nos importa el indice
    print(nombre)
for i in range(len(listaNombre)):#* sinos interesa la posición y el contenido
    print(i,"-",listaNombre[i])


for i, nombre in enumerate(listaNombre): #* esta forma son equivalente a las otras 2
    print(i,"-",nombre)

num1 = [4]
num2 = num1.copy() #*esto crea una copia o crear una lista nueva
num2[0] *= 2
print(num1) #* no asignas nueva línea, sino que crea una referencia