#* Bloques para las excepciones
from cupsext import cancelJob
correcto = False
while correcto!=True:
    try:
        numero = int(input("Introduce un numero y positivo: "))
        resultado = 10/numero
        assert numero>=0,"No admito numero negativos" #!otro tipo de excepción personalizada, excepción debe ser falso,mensaje opcional
        """if numero < 0:
            raise Exception("No es un numero positivo")"""#! es una excepción pesonalizada por nosotros mismo
    except ZeroDivisionError: #! puedes personalizar las execepciones, no pode divirdir por 0
        print("⚠️ Has intentado devidir un numero por '0' ⚠️")
    except ValueError: #! no es exatamente lo que pides
        print("⚠️ Error, debemos meter una letra o un valor que no sea un numero entero ⚠️")
    except:
        print("⚠️ Execepcion, pero otra ⚠️")
    else: #*Opcional, se ejecuta en el caso de que no ocurra una excepción
        print(resultado)
        correcto = True
    finally: #* opcional, se ejecuado siempre que try funcione como que exista una excepción
        print("Seguimos adelante...")
print("programa finalizado")

#*BLOQUES OPCIONALES
#*Bloque Else
#*Bloque Finally
#*CONTROL DE EXCEPCIONES
#*
#*ERRORES PERSONALIZADOS: con raise

