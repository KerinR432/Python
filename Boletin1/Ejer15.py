import random
#EJERCICIO 15
print("****************************************")
num1 = int(input("Introduce un numero")) #--> pedimos un numeroo por patalla.
num2 = int(input("Introduce un segundo numero"))

if num1 > num2: #--> una coondición que si un numeroo es mayor es el que estara al final del random.
    rsdo = random.randint(num2,num1)
else: # --> y si no se cumple entrara aqui y el que solo queda invertir el resultado.
    rsdo = random.randint(num1,num2)
print(rsdo) # --> imprimimos el resultado por pantalla.