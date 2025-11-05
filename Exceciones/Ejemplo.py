#* Bloques para las excepciones
try:
    numero = int(input("Introduce un numero: "))
    resultado = 10/numero
    print(resultado)

except:
    print("Ha ocurrido un excepción")

else: #*Opcional, se ejecuta en el caso de que no ocurra una excepción
    print("Todo bien")
finally: #* opcional, se ejecuado siempre que try funcione como que exista una excepción
    print("Seguimos adelante...")
print("programa finalizado")

#*BLOQUES OPCIONALES
#*Bloque Else
#*Bloque Finally