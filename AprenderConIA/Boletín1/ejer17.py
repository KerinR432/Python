import random

# !EJERCICIO: Simulación de resultados de quiniela

# *Lista para almacenar los resultados de la quiniela (valores entre 1 y 3)
resultadosQuiniela = []

# ?Generar los resultados aleatorios de la quiniela y sustituir los 3 por 'x'
for i in range(15):
    resultado = random.randint(1, 3)  # Generar un número aleatorio entre 1 y 3
    if resultado == 3:
        resultado = 'x'  # Sustituir 3 por 'x'
    resultadosQuiniela.append(resultado)

# //Mostrar los resultados finales
print("=====================================")
print("Resultados de la Quiniela:")
for i, resultado in enumerate(resultadosQuiniela, start=1):
    print(f"Día {i}: {resultado}")
print("=====================================")
