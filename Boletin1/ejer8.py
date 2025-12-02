"""
 8. Escribir un programa que reciba por teclado el importe de una cantidad a pagar en euros
(puede tener decimales) y el número de meses que contamos para pagarla (tiene que ser un
número entero) y nos devuelva el dinero que tendríamos que pagar cada mes. No aplicamos
intereses de ningún tipo y redondeamos a dos decimales.
"""

correcto = False

while correcto !=True:
    try:
        pagar = float(input("Introduce el importe a pagar en euros: "))
        meses = int(input("Introduce el número de meses: "))

        if pagar <= 0:
            raise ValueError("El importe debe ser mayor que 0.")
        if meses <= 0:
            raise ValueError("El número de meses debe ser un entero positivo.")

        apagarCadaMes = round(pagar / meses, 2)
    except ValueError as e:
        print("Error:", e)
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
    else:
        print(f"Durante {meses} meses tienes que pagar cada mes: {apagarCadaMes} €")
        correcto = True

