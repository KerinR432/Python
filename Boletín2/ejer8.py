"""8. Escribe un programa que pida un número por teclado y escriba todos sus divisores
separados por comas (y evitando poner una coma al final). Por ejemplo, si el número
introducido es el 14 tu programa debería de mostrar lo siguiente"""

num = int(input("Introduce un numero: \n"))

for i in range(1,num+1):
    if num % i ==0:
        print(f"{i},",end=" ")