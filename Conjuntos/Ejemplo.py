conjunto1 = {"Ana","Pedro","Luis","Eva","Ana"}#* no lo almacena por orden, más bien van variando cada vez
#*No varia. No permite tener dos mismas variables
print(conjunto1)
conjunto2 = set(["Ana","Pedro","Luis","Eva","Ana"]) #* Otra forma de llamar y combierte una lista en un conjunto
print(conjunto2)

for nombre in conjunto1:#* Podemos recorrer el conjunto asi
    print(nombre)

if "Ana" in conjunto1:  #* sí que se puede hacer una condición donde podremos ver si existe un nombre u otro elemento
    print("Ana esta")

print(len(conjunto1))

conjunto1.add("Manuel")
conjunto1.add("Manuel") #* Añadir elemento
print(conjunto1)
conjunto1.remove("Ana") #* Eliminar elementos
print(conjunto1)
conjunto1.discard("Eustaquio")#* si eliminamos algo que no existe, da error. Pero con 'discard' si puede eliminar

print(conjunto1.pop()) #* Eliminamos el primero, nos lo recupera, pero de manera aletoria
print(conjunto1)

conjunto1.clear() #* Elimina todo el conjunto
print(conjunto1)

profesPrimero = {"Natalia","José María","Pedro","Yago"}
profesSegundo =  {"José María","Agustín","Puche","Pedro"}
print(profesPrimero & profesSegundo) #* intercepción, nos devuelve los dos profesores repitos en el conjunto, los comunes
print(profesPrimero | profesSegundo)#* la unión consegui todos pero se consigue una ves
print(profesSegundo - profesPrimero)#* la diferencia
print(profesPrimero - profesSegundo)#* quita los que se repite o lo que no estan el común