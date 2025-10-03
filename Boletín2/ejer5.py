"""5. Escribir un programa que nos pida las notas obtenidas en un trimestre y nos muestre la
media ponderada sabiendo que;
1. La primera nota corresponde al trabajo en clase y cuenta como un 5% del total
2. La segunda corresponde a los ejercicios prácticos: 15%
3. La tercera la nota del examen: 80%
El resultado debería de mostrarse de dos formas: redondeado con dos decimales (nota
real) y sin redpmdeada sin decimales (nota de boletín)."""

# Pedimos por teclado
notaT = float(input("Intorduce la nota de los trabajos en clases: \n"))
notaJ = float(input("Introduce la nota de los trabajos practicos: \n"))
notaE = float(input("Introduce la nota de los examenes:\n"))

# Creamos variables que no varian
cincoPor = 0.05
quincePor = 0.15
ochentaPor = 0.80

# creamos la operación

rsdo = notaT * cincoPor
rsdo2 = notaJ * quincePor
rsdo3 = notaE * ochentaPor

# Mostramos el resultado
print(f"tu nota de tranajo en clases es: {notaT}  y el resultado es :{round(rsdo, 2)} y tu nota real es : {int(rsdo)}")
print(f"tu nota de tranajo en clases es;{notaJ}  y el resultado es :{round(rsdo2, 2)} y tu nota real es : {int(rsdo2)}")
print(f"tu nota de tranajo en clases es;{notaE}  y el resultado es :{round(rsdo, 3)} y tu nota real es : {int(rsdo3)}")
