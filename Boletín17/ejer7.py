def cargar_datos():
    policia = {}  # Diccionario para guardar todo
    criminal_actual = None

    try:
        with open("delincuentes.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea: continue  # Saltamos líneas vacías

                if linea.startswith("- "):
                    # Es un nombre. Formato: "- Diego Norrea, 35"
                    # Quitamos el "- " del principio y separamos por la coma
                    parte_nombre = linea.replace("- ", "")
                    nombre, edad = parte_nombre.split(",")

                    criminal_actual = nombre.strip()
                    # Creamos una entrada en el diccionario con la edad y una lista vacía para delitos
                    policia[criminal_actual] = {
                        "edad": edad.strip(),
                        "delitos": []
                    }
                else:
                    # Es un delito. Se lo añadimos al criminal actual
                    if criminal_actual:
                        policia[criminal_actual]["delitos"].append(linea)
        return policia
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return {}


# --- PROGRAMA PRINCIPAL ---

datos_policia = cargar_datos()

sospechoso = input("Introduce el nombre del ciudadano: ")

if sospechoso in datos_policia:
    # Si existe, mostramos sus datos
    print(f"Edad: {datos_policia[sospechoso]['edad']} años")
    print("Antecedentes penales:")
    for delito in datos_policia[sospechoso]["delitos"]:
        print(f"- {delito}")
else:
    # Si no está en el diccionario
    print("Sin antecedentes penales")