"""21. Escribir un programa que pida por teclado un número al usuario y calcule si es primo o no"""

#pedimos una variable
num1 = int(input("Introduce un numero "))

num2 = int(num1** .5)+1
primo = True
for i in range(2,num2):
    if num1%i==0:
        primo = False

print(primo)