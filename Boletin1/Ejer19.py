#declaramos variables
#? declarar metodos
def calcularDivisores(num):
    # recorremos el bucle del numero para sacar el divisor
    divisores = []
    for i in range(1, num + 1):
        if (num % i) == 0:
            divisores.append(i)
    return divisores


#* declarar Variables
numero = 0
salir = False
while not salir:
    try:
        numero = int(input("Introduce un numero: "))

        if numero <= 0:
            raise Exception("Error no debe ser un numero negativo.")
        listaDivisoresTexto = str(calcularDivisores(numero))
        listaDivisoresTexto = listaDivisoresTexto.replace("["," ")
        listaDivisoresTexto = listaDivisoresTexto.replace("]", " ")
        listaDivisoresTexto = listaDivisoresTexto.replace(",", " || ")
    except Exception as ex:
        print(ex)

    except ValueError:
        print("Numero invalido")
    except:
        print("Error")

    else:
        formato= f"""
    =========================
    CALCULADORA DIVISORES
    =========================
    LOS DIVISORES DEL NUMERO:
    {numero}
    SON LOS SIGUIENTES:
    {listaDivisoresTexto}
"""
        print(formato)
        print("saliendo...")
        salir = True