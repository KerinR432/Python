import random
#EJERCICIO 14

salir = False
while salir == False:
    try:
        print("****************************************")

        num1 = int(input("Introduce un numero"))
        num2 = int(input("Introduce un segundo numero"))
        if num1 == 0 and num2 == 0:
            s
    except ValueError:
        print("Introduce un numero entero")
    except ZeroDivisionError:
        print("No puedes introducir un numero: '0'")
    else:
        rsdo = random.randint(num1, num2)
        salir = True
print(rsdo)