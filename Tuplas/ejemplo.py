lista = [1,2,3]  # * la forma de crear una lista '[]'
tupla = (1,2,3) # * la forma de crear una tupla es '()'
tupla2 = ("ana","Pepe","Pedro") #* puede ser String
tupla3 = ("Maria",28.5,False) #* Y dejar de ser eterogenea
tupla4 = 4,5,6 #*Esto se entiende como una tupla aunque no tenga '()'

#* se mostrará los '()'
print(tupla)
print(tupla4)
tupla5=()#* se puede crear una tupla vacía, pero es extraño, no se puede modificar, asi que no se necesita
pi = (3.14159) #* no se puede crear una tupla con un solo valor, no detecta como un número
p2 = (3.14159,)#* de esta manera podemos crear un solo valor con tuplas
print(pi)
#*Se puede convertir entre tupla a lista
tupla6 = tuple(lista) #! de list a tupla
print(tupla6)
lista2 = list(tupla4)#! de tupla a lista
print(lista2)
#* podemos pasarlo a una cadena de caracteres
texto = str(tupla6)
print(texto)

tupla7 = (1,2,(1,3,4),5,[1,2,3],7) #* se puede crear tuplas anidadas, hasta puede tener una lista dentro de esa tupla
print(tupla7) #* se puede modificar el contenido de la lista que hay dentro de la tupla

print(tupla7[-2]) #*admite las referencia negativas, como una lista
tupla7[4][0] = 23 #* permite modificar esa lista dentro de la tupla
print(tupla7[4])