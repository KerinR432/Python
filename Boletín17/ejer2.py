def calcular_estadisticas():
    # 1. Preparamos nuestras "cajas" (variables) para guardar datos
    total_hombres = 0
    total_mujeres = 0
    suma_alturas = 0.0
    cuenta_total = 0

    # Esta variable nos ayuda a saber qué estamos leyendo
    # True = Género, False = Altura
    toca_leer_genero = True

    try:
        # 2. Abrimos el archivo de forma segura
        with open("estadisticas.txt", "r") as archivo:
            for linea in archivo:
                # Quitamos espacios o saltos de línea invisibles
                dato = linea.strip()

                if not dato: # Si la línea está vacía, la saltamos
                    continue

                if toca_leer_genero:
                    # Lógica para contar géneros
                    if dato == "Hombre":
                        total_hombres = total_hombres + 1
                    elif dato == "Mujer":
                        total_mujeres = total_mujeres + 1

                    # El siguiente dato será una altura
                    toca_leer_genero = False
                else:
                    # Lógica para procesar la altura
                    altura_num = float(dato)
                    suma_alturas = suma_alturas + altura_num
                    cuenta_total = cuenta_total + 1

                    # El siguiente dato volverá a ser un género
                    toca_leer_genero = True

        # 3. Cálculos finales y mostrar resultados
        if cuenta_total > 0:
            media = suma_alturas / cuenta_total
            print("Hombres:", total_hombres)
            print("Mujeres:", total_mujeres)
            print("Estatura media:", round(media, 2))
        else:
            print("El archivo estaba vacío.")

    except FileNotFoundError:
        print("Error: No encontré el archivo 'estadisticas.txt'")

# Ejecutar la función
calcular_estadisticas()