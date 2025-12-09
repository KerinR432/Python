# 8. Escribir un programa que reciba por teclado el importe de una cantidad a pagar en euros
# (puede tener decimales) y el número de meses que contamos para pagarla (tiene que ser un
# número entero) y nos devuelva el dinero que tendríamos que pagar cada mes. No aplicamos
# intereses de ningún tipo y redondeamos a dos decimales.

# Usamos un bucle 'while True' infinito. Solo saldremos del bucle con 'break'
# si la entrada de datos es completamente correcta y validada.
while True:
    try:
        # 1. Petición de entradas y conversión de tipos
        pagar = float(input("Introduce el importe total a pagar en euros (ej: 150.50): "))
        meses = int(input("Introduce el número de meses para el pago (ej: 12): "))

        # 2. Validaciones lógicas
        if pagar <= 0:
            # Lanzamos un error si el importe es inválido
            raise ValueError("El importe total a pagar debe ser mayor que 0.")

        if meses <= 0:
            # Lanzamos un error si el número de meses es inválido
            raise ValueError("El número de meses debe ser un entero positivo (mayor que 0).")

        # 3. Cálculo y redondeo (si las validaciones anteriores pasaron)
        pago_mensual = round(pagar / meses, 2)

    except ValueError as e:
        # Captura errores de tipo (float/int) y errores de validación lógica (raise ValueError)
        print(f"\n--- ERROR DE ENTRADA ---\n{e}\n")

    except ZeroDivisionError:
        # Aunque el 'if meses <= 0' lo previene, lo dejamos como capa de seguridad
        print("\n--- ERROR DE CÁLCULO ---\nNo se puede dividir el pago entre cero meses.\n")

    else:
        # El bloque 'else' se ejecuta si el 'try' fue exitoso (sin excepciones)
        # 4. Presentación de resultados
        print("\n--- RESULTADO DEL PLAN DE PAGO ---")
        print(f"Importe total a pagar: {pagar:.2f} €")
        print(f"Plazo: {meses} meses")
        print(f"El importe que tendrías que pagar cada mes es: {pago_mensual:.2f} €")

        # 5. Salida del bucle (la entrada fue correcta)
        break