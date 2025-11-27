"""
6. Una clave con el siguiente formato XX00-xxX-00 donde las X deben de ser letras
mayúsculas, las x letras minúsculas y los 0 dígitos.
Ejemplo: AB12-xyZ-75
"""
import re

textoClave = "AB12-xyZ-75"

textoCorrecto = f"""
TU TEXTO SECRETO ES ESTO
"""
textoIncorrecto = f"""
ERROR ESTAMOS BUSCANDO EL FALLO...
"""
patronMayus = r"[A-Z]"
patronMinus = r"[a-z]"
patronDigito = r"[0-9]"

if re.match(patronMayus,textoClave):
    textoClave = textoClave.replace(patronMayus,"X")
    print(textoClave)