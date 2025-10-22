"""12. Las matrículas españolas constan de un número de cuatro dígitos y tres letras
cualesquiera en mayúsculas a excepción de las vocales, la Ñ y la Q. Escribe un
programa que detecte si una matrícula introducida por teclado es válida o no."""

matricula = input("Introduce la Matricula 🚘\n")

matricula.lower()
if len(matricula) == 8:
    print("Primer paso correcto ✔️")

digitos = matricula[0:4]
num = sum(c.isdigit() for c in matricula)
print(digitos)

if num == 4:
    print("Bien, son 4 digitos")
else:
    print("no tiene 4 digitos")

if matricula:
