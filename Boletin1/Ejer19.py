#declaramos variables
num = 0
divisores = []
# pediimos por teclado
num = int(input("Introduce un numero. "))

# recorremos el bucle del numero para sacar el divisor
for i in range(1,num+1):
    if (num % i)==0:
        divisores.append(i)

#Mostramos el array
print(f"los divisores son: {divisores}")
