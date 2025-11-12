from Xlib.Xcursorfont import pirate

salir = False

while salir != True:
    try:
        final = 128
        binario = list()

        decimal = int(input("Introduce un numero decimal: "))
        assert decimal <= 225
        assert decimal > 0

    except ValueError:
        print("El numero debe ser un numero")

    except:
        print("El numero debe ser positivo")


    else:
       for i in range(1,9):
            if decimal >= final:
                decimal = decimal-final
                binario.append(1)

            elif final == 0 and decimal == 1:
                binario.append(1)
            else:
                binario.append(0)
                final = final // 2
    salir = True
print(binario)