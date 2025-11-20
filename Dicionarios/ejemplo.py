#* Dos formas de declarar un diccionario
dict1 = {"Nombre" : "Jose Maria", "Edad" : 57, "Activo" : True}
dict2 = dict(color="azul",modelo="Canddy",submodelo="Outdoor",motor=2.0)

#* las dos formas de arribar son las dos formas de rellenarlo
print(dict1)
print(dict2)

#! la clave puede ser cualquier cosa, sea String o digito. Las claves no puede estar repetidas, sustituye el valor anterior.
dict3 = {24:"Charcuteria Mano",26:"Medias Puri",28:"Bar el Torrezno"}
print(dict3)

#* recuperar el valor, seria pasar el nombre de dicho valor.
print(dict3[26])
print(dict2["modelo"])
#TODO get si no encuentra lo que buscamos, nos devuelve que no existe esa clave.
print(dict2.get("motor"))

#* aqui se muestra 3 formas de recorrer el diccionario. Una la claves,el segundo los elemento y el tercero los 2
for elemento in dict3:
    print(elemento)

for elemento in dict3:
    print(dict3[elemento])

for elemento in dict3:
    print(elemento,dict3[elemento])


#! esto es una forma de mostrar todo el Diccionario, intems devuelve una lista de tuplas, los otros 2 devuelve una lista
#!apartir de aquí tocara aprender o usarlos
print(list(dict3.keys()))
print(list(dict2.values()))
print(list(dict1.items()))

#*Asi es como se crea o se introduce un nuevo dato en el diccionario, si el valor existe, elimana el anterior. lo Remplaza
dict3[30] = "Peluqueria Canina el galgo"
print(list(dict3.items()))

#*Update permite actualizar un diccionario a partir de otro
dict4 ={"activo":False, "dni":"28777666x","telefono":655543322}
dict1.update(dict4)
print(list(dict1.items()))

#! .clear() borrar el diccionario completamente
#dict1.clear()
print(dict1)

#! elimina y devuelve el valor de la clave que le pasemos al diccionario.
dict1.pop("Edad")
print(dict1)

#! deuvelve la tupla completa y el valor elimando. Elimina el ultimo elemento.
dict1.popitem()
print(dict1)