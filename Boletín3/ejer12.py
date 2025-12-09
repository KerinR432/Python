"""12. Las matrículas españolas constan de un número de cuatro dígitos y tres letras
cualesquiera en mayúsculas a excepción de las vocales, la Ñ y la Q. Escribe un
programa que detecte si una matrícula introducida por teclado es válida o no."""
import re

#* declarar variable
patron = r"[0-9]{4}[B-DF-H-J-N-P-RST-V-Z]{3}"


try:
    matricula = "4325AFG"

    if re.fullmatch(patron, matricula):
        print("Funciona")
    else:
        assert