"""
 8. Escribir un programa que reciba por teclado el importe de una cantidad a pagar en euros
(puede tener decimales) y el número de meses que contamos para pagarla (tiene que ser un
número entero) y nos devuelva el dinero que tendríamos que pagar cada mes. No aplicamos
intereses de ningún tipo y redondeamos a dos decimales.
"""

def calcularPagoAlMes(pagar,meses):
    return round(pagar / meses, 2)

salir = False

while salir !=True:
    try:
        pagar = float(input("Introduce el importe a pagar en euros: "))
        meses = int(input("Introduce el número de meses: "))

        if pagar <= 0:
            raise ValueError("El importe debe ser mayor que 0.")
        if meses <= 0:
            raise ValueError("El número de meses debe ser un entero positivo.")

        apagarCadaMes = calcularPagoAlMes(pagar,meses)

        factura = f"""
        -- FACTURA --
        DEBES PAGAR {pagar:.2f}€
        DURANTE {meses} MESES
        EN TOTAL PAGAS AL MES
        -- {apagarCadaMes:.2f}€ --
        """
    except ValueError as e:
        print("Error:", e)
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
    else:
        print(factura)
        salir = True

