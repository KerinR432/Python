import random

# EJERCICIO 12: Simulador de Lanzamiento de Dados
print("======================================")


# * ------------------------- FUNCIONES ------------------------------
def dadosAletorios(cantidadDados: int, cantidadCaras: int, dados: list):
    """
    Genera y muestra una tirada aleatoria de dados.

    Realiza el lanzamiento de la cantidad especificada de dados
    y muestra un informe del resultado.

    Args:
        cantidadDados (int): El número de dados a lanzar.
        cantidadCaras (int): El número de caras que tiene cada dado (ej: 6, 12, 20).
        dados (list): Una lista vacía que se llenará con los resultados de las tiradas.
    """
    # El guion bajo (_) se usa ya que no necesitamos la variable de iteración.
    # El bucle se repite tantas veces como 'cantidadDados'.
    for _ in range(cantidadDados):
        # Rellenamos la lista 'dados' con un número aleatorio entre 1 y el número de caras.
        dados.append(random.randint(1, cantidadCaras))

    informe = f"""
    Se han lanzado: {cantidadDados} dados
    Con {cantidadCaras} caras
    El resultado de las tiradas es:  {dados}
"""
    print(informe)


# * ------------------------ LA LOGICA ------------------------------
# Variable de control para saber si debemos salir del bucle principal.
salir: bool = False

# Bucle principal: sigue pidiendo datos hasta que 'salir' sea True.
while not salir:
    # Usamos try-except para manejar errores y evitar que el programa se detenga.
    try:
        # Petición de datos al usuario
        cantidadDados = int(input("Introduce el número de dados que quieres lanzar: "))
        dados = []  # Lista para almacenar los resultados de las tiradas.
        cantidadCaras = int(input("Introduce el número de caras de los dados: "))

        # Validaciones de entrada: los números deben ser positivos.
        if cantidadDados <= 0:
            # Lanzamos una excepción para que sea capturada abajo
            raise ValueError("La cantidad de dados debe ser un número positivo.")
        if cantidadCaras <= 0:
            # Lanzamos una excepción para que sea capturada abajo
            raise ValueError("La cantidad de caras debe ser un número positivo.")

        # Llamada a la función para ejecutar la lógica.
        dadosAletorios(cantidadDados, cantidadCaras, dados)

    # Captura errores cuando el usuario no introduce un número entero.
    except ValueError as e:
        # Mostramos el error específico (ya sea de la función int() o el que lanzamos en el 'if').
        print(f"Error de entrada: {e}")

        # Se ejecuta si no hubo ninguna excepción en el bloque 'try'.
    else:
        print("Saliendo del programa...")
        # Cambiamos la variable de control para terminar el bucle 'while'.
        salir = True