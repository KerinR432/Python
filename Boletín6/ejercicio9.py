"""
 9. Un número de 4 cifras mínimo y 8 cifras máximo
 Ejemplo: 12345
"""
import re

correcto = f"""
BIEN GENIAL, HAS INTRODUCIDO
LOS NUMERO CORRRECTAMENTE.
"""

numero = "12345678"
patron = "[0-9]{4,8}$"

if re.match(patron,numero):
    print(correcto)
else:
    print("salgo")