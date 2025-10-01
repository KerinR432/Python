#PRIMER PARAMETRO
print("---PRIMERO PARAMETRO---")
texto = "Hola mundo" # un String 😁.
print(texto[3:8]) # Sintaxis bocadillo🥪, toma una porción de la subcadena que empieza en la posción 3 y termina en la posición 7
#SEGUNDO PARAMETRO
print("---SEGUNDO PARAMETRO---")
texto2 = "Hola mundo"
print(texto2[3]) #Solo pillas una letra🥪
texto3 = "Hola mundo"
print(texto3[-5:-2]) #recorre cadenas al reves,empiezan al final
texto4 = "Hola mundo"
print(texto4[2:-2]) #se pueden mezclar ambos

#TERCER PARAMETRO
print("---TERCER PARAMETRO---")
texto5 = "Hola mundo"
print(texto5[2:-2:2]) # el tercer parametro especifica cuanto saltos debe dar la cadena
print("--pares--")
print(texto5[::2]) #caracteres pares
print("--impares--")
print(texto5[1::2]) #caracteres impares
print("---DAR LA VUELTA---")
print(texto5[::-1])#Empieza la cadena al reves
print((texto5[::-2]))# Empieza al raves de dos en dos
#concatenar
print("---CONCATENAR---")
texto6 = "Hola"+"mundo"+"cruel"+str(33)#el str lo convierte en String
#recorrer una cadena
print("--recorrer una cadena--")
print(texto6)
for caracter in texto6:
    print(caracter,end="-")# recorrer la cadena caracter a caracter

print("\n",len(texto6))#la función 'LEN' devuelve la longitud de lo que sea

for position in range(0, len(texto6)):
    print(position, "-", texto6[position])#saber la posción de cada cadena

print("Hola", "mundo", "cruel")#se puede concatener en el print con comas
print("Hola" + "mundo" + "cruel")
texto6 = "Hola", "mundo", "cruel" #tupla crea una tupla
print(texto6)

#METODOS DE CADENAS
print("---METODOS---")
texto7 = "Hola mundo cruel 33"
print("--mayusculas--")
print(texto7.upper()) #texto todo en mayusculas
print("--minusculas--")
print(texto7.lower()) #texto todo en minusculas
print("--combinado--")
print(texto7.swapcase()) #texto combinación de mayusculas y minusculas
print("--devuelve posición--")
print(texto7.find("m")) #devuelve la posción del caracter, -1 si no existe y si son 2 caracteres devulve el primero

print("--mayusculas, combinando con sintaxis bocadillos 🥪 --")
print(texto7[2:4].upper()) #texto todo en mayusculas
print("--devuelve cuantas veces aparece")
print(texto7.count("o")) #devuelve cuantas veces aparece
print("--remplazar--")
print(texto7.replace(" ","")) #sustituye un caracter o una subcadena en la cadena original
print("--Busca la segunda posición--")
print(texto7.find("o"))
print(texto7.find("o",2)) #devuelve la la segunda "o" en la busqueda 🔍
print("--replanza el N de espacio--")
print(texto7.replace(" ","x",1)) #Solo sustituye los primeros N caracteres de la cadena
