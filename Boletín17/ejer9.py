try:
    with open("alumnos.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # 1. Separamos el nombre de las notas usando el ": "
            partes = linea.strip().split(": ")
            nombre_completo = partes[0]
            notas_texto = partes[1]

            # 2. Convertimos la cadena de notas en una lista de números (floats)
            # Separamos por ", " y convertimos cada trozo a número
            notas = [float(n) for n in notas_texto.split(", ")]

            # 3. Comprobamos si TODAS las notas son >= 5
            # La función all() devuelve True si se cumple la condición para todos
            if all(nota >= 5 for nota in notas):
                # 4. Calculamos la media: (Suma de notas / cantidad de notas)
                media = sum(notas) / len(notas)

                # 5. Formateamos el nombre (Apellido, Nombre -> Nombre Apellido)
                # Separamos por la coma que hay en el nombre
                apellido, nombre = nombre_completo.split(", ")

                # 6. Imprimimos resultado redondeando a 1 decimal
                print(f"{nombre} {apellido} – {round(media, 1)}")

except FileNotFoundError:
    print("Error: El archivo 'alumnos.txt' no existe.")