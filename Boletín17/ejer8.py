import random

# Listas iniciales
nombres = ["Ash", "Momo", "Monkey", "Naruto", "Nico", "Ken", "Roronoa", "Touka"]
apellidos = ["Ketchum", "Ayase", "D. Luffy", "Uzumaki", "Robin", "Kaneki", "Zoro", "Kirishima"]

try:
    # Pedimos el número y lo convertimos a entero
    cantidad = int(input("Cuantos personajes tendrá tu partida: "))

    # Validación de rango (1-8)
    if cantidad < 1 or cantidad > 8:
        print("Error: El número debe estar entre 1 y 8.")
    else:
        # Mezclamos las listas aleatoriamente
        random.shuffle(nombres)
        random.shuffle(apellidos)

        personajes_generados = []

        print("Personajes:")
        # Bucle para crear los personajes solicitados
        for i in range(cantidad):
            # Combinamos el nombre y apellido que están en la misma posición
            nombre_completo = f"{nombres[i]} {apellidos[i]}"
            print(nombre_completo)
            personajes_generados.append(nombre_completo)

        # Crear el archivo y guardar los nombres
        with open("personajes.txt", "w", encoding="utf-8") as archivo:
            for p in personajes_generados:
                archivo.write(p + "\n")

        print("\nArchivo 'personajes.txt' generado con éxito.")

except ValueError:
    # Si el usuario introduce letras en lugar de un número
    print("Error: Debes introducir un número entero válido.")