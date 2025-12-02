"""
16. Escribe un programa que pida por teclado el radio de una circunferencia, admitiendo
valores con decimales y calcule la longitud y el área de la circunferencia (redondeando
a cinco decimales). Si no las recuerdas, las fórmulas son las siguientes:
 area = 3.14159 * radio2
 longitud = 2 * 3.14159 * radio
"""

PI = 3.14159
area = 0
longitud = 0
salir = False

while salir != True:
    try:
        radio = int(input("Ingresa un numero entero: "))

        area = round(area, 5)
        longitud = round(longitud, 5)

        if radio <= 0:
            raise ValueError("EL radio no puede ser negativo")

    except ValueError as e:
        print("Error:",e)
    except ZeroDivisionError as e:
        print("Error:",e)
    else:
        area = PI * (radio * radio)
        longitud = 2 * PI * radio
        print(f"""
        El radio del circulo es {radio}
        Bien calculado...........
        -------------------------------
        el area es: {area}
        La longitud es: {longitud}
        """
              )
        salir = True