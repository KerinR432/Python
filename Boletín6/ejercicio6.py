"""
6. Una clave con el siguiente formato XX00-xxX-00 donde las X deben de ser letras
mayúsculas, las x letras minúsculas y los 0 dígitos.
Ejemplo: AB12-xyZ-75
"""
import re

textoClave = input("Introduce un texto: ")

textoCorrecto = f"""
TU TEXTO SECRETO ES ESTO
"""
textoIncorrecto = f"""
ERROR ESTAMOS BUSCANDO EL FALLO...
"""
listaMayuscula = [f"ABCDEFGHYJKLMÑNOPQRSTVUXYZ"]
patron = r"[A-Z]"
patronmin = r"[a-z]"
patronDigito = r"[0-9]"

if re.match(patron,textoClave):
    textoClave = re.sub(patron,"X",textoClave)
    if(re.search(patronmin,textoClave)):
        textoClave = re.sub(patronmin,"x",textoClave)
    if(re.search(patronDigito,textoClave)):
        textoClave = re.sub(patronDigito, "0", textoClave)


print(textoClave)