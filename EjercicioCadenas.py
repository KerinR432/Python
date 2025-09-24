texto = input("Introduce un texto: ")
texto2 = " "
for c in texto:

    if c != " ":
        texto2+=c

print(texto2,end="")

## bucle WHILE
print("--------------------------------")
i = 0
while i < 10:
    print(i)
    i+=1

##RANDOM
#--> poner in import para llaamar una libreria
import random
print("------------------------------")
azar = random.randint(1,6) ## el ultimo numero si se toma en cuenta
print(azar)

##REDONDERAR UN NUMERO
print("--------------------------------------")
pi = 3.14159
print(round(pi,2))
print(round(pi,3))
print(round(pi,4))
print(pi)

print("-------------------------------------")
for _ in range(0,5): #cuando la variable no se va usar en el for es "_" se usa mucho cuando no utilizas el indice
    print(random.randint(1,6))

for i in range(0,5): #cuando la variable no se va usar en el for es "_" se usa mucho cuando no utilizas el indice
    azar = random.randint(1,6)
    print(azar)
print("=====================================")
print(i)
print(azar)