"""
 8. Escribir un programa que reciba por teclado el importe de una cantidad a pagar en euros
(puede tener decimales) y el número de meses que contamos para pagarla (tiene que ser un
número entero) y nos devuelva el dinero que tendríamos que pagar cada mes. No aplicamos
intereses de ningún tipo y redondeamos a dos decimales.
"""

correcto = False

while correcto !=True:
    try:
        pagar = float(input("Introduce un numero a pagar... "))
        meses = int(input("Intorduce numero de meses... "))
        apagarCadaMes = pagar / meses
        assert meses >= 1,"No puede ser numeros decimales"
        assert pagar >= 1, "No puede ser numeros decimales"
    except ZeroDivisionError:
        print("Error no puedes dividir por cero caballero , haga el favor de hacerlo bien")
    except:
        print("Error no puedes introducir numeros negativo o deciamales")
    else:
        print(f"durante {meses} meses tienes que pagar cada mes: {apagarCadaMes}€")
        correcto = True


