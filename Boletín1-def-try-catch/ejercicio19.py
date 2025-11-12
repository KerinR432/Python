num = 0
divisores = []
salir = False
# pediimos por teclado
def sacarDivisores (num):
    for i in range(1, num + 1):
        if (num % i) == 0:
            divisores.append(i)
    return divisores

while salir != True:
    try:
            num = int(input("Introduce un numero. "))
            assert num >=0
            assert num != 0

    except ZeroDivisionError :
        print("El numero no debe de ser `0` ")

    except ValueError:
        print("El numero debe ser un numero entero")

    except:
        print("Excepciones, tienes mas errores")

    else:
        divisores = sacarDivisores(num)
        salir = True
        print(f"los divisores son: {divisores}")

    finally:
        print("Sigue adelante")


