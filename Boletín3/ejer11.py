"""11. Mejorar el programa anterior para que detecte si se trata de un NIF o un NIE y nos
comunique, además de si es válido de que tipo es Un NIE es una cadena de 9 caractéres que siempre empieza por X,Y o Z y a
continuación vienen 7 cifras y una letra final. Las letras inicial y final pueden estar
escritas con mayúsculas o con minúsculas
"""

dato = input("Introduce tu DNI\n")
canDigito = sum(c.isdigit() for c in dato)
letras = "xyz"

if canDigito == 7:
    print("NIE: Bien has pasado primera seguridad")
else:
    print("Error❌")
if dato.find(letras) != -1:
    print("NIE: Bien has pasado el segundo punto")
else:
    print("Error❌")



if len(dato) ==9:
    print("Bien primera seguridad cumplida")
else:
    print("Error❌")

if canDigito == 8:
    print("Bien has pasado el segundo punto de seguridad")
else:
    print("Error❌")
