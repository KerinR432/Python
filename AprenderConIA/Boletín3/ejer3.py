"""Programa que pide el nombre y los apellidos del usuario y los muestra formateados
en el estilo: Apellidos, Nombre."""

# Pedimos los datos al usuario
nombre = input("Introduce tu nombre: ").strip().title()
apellidos = input("Introduce tus apellidos: ").strip().title()

# Mostramos el nombre formateado
print(f"\nTu nombre formateado es: {apellidos}, {nombre}")
