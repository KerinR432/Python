"""24. Modifica el programa anterior para que sea el usuario quién introduzca dos números y se nos
muestre los primos que hay entre ambos"""

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un segundo numero: "))

for x in range(num1,num2):
    primo = True
    for i in range(2,int(x**.5)+1):
        if x%i==0:
            primo = False
    if primo:
        print(x)