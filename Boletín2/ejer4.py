"""
4. Escribir un programa que nos pida por teclado dos calificaciones numéricas de un
alumno y nos muestre la media aritmética resultante redondeada sin decimales. Las
notas introducidas deben de estar entre 0 y 10 y admiten decimales. Caso de que una
entrada sea errónea debería de advertirnos de ello y no hacer el cálculo
"""
#Inicializamos las variables
nota =  float(input("Introduce una nota:\n"))
nota2 = float(input("Introduce una segunda nota: \n"))

#uan condición donde las dos variables deben ser de 0 a 10
if(nota>= 0 and nota <=10 and nota2>=0  and nota2<=10):
    rsdo = int((nota + nota2)/2) #la operación de proemdio📖
    print(f"El resultado del alumno x es:  {rsdo}")
else: #sino funciona devuelve otra cosa
    print("Mal, debes introducir numeros de 0 al 10...")
