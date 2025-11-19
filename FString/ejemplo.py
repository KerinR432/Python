#* veremos ahora el formato F''
nombre = "Moha"
edad = 21
sueldo = 10000.501
#* En un print normal y corriente, puedes hacer un cadena que no se interrumpe el string y luego pones las variables
#*con %
print('Mi nombre %s,tengo %d años y cobro %.2f euros al mes' % (nombre, edad, 1000.501))
#*Fstring
#*forma 1
print(f"mi nombre {nombre} tengo {edad} años y cobro {sueldo} euros al mes")#* la varibale se pone entre corchete
#*forma 2
#*modificadores
print(f"mi nombre {nombre} tengo {edad} años y cobro {sueldo : .2f} euros al mes")
#*formato 3
#*el '%' calcula el porcentaje del número y puedes poner él cuantos decimales, siempre redondea
ratio = 0.08394
print(f"Porcentajes: {ratio:.2%}")
#formato 4
#* separador de millares
habitantes = 712670000
print(f"Población: {habitantes:,} habitantes")
#*reserva espacio o con espacio en ese número
num1=45
num2=123
print(f"{num1: 4d}\n{num2: 4d}")
#*formato 5
texto = "Python"
#*alinea el texto en la izquierda a 20 espacios o derecha o en el centro
print(f"***{texto:<20}****")
print(f"***{texto:>20}****")
print(f"***{texto:^20}****")
#*formato 6
#*nos muestra el nombre de la variable y el tipo
print(f"{num1=}\n{num2=}\n{texto=}")
#*formato 6
#*un fString que ocupa mas de una linea de texto
ficha=f"""
ficha del profesor/a:
=====================
Nombre: {nombre}
_____________________
edad: {edad}
_____________________
Salario:{sueldo:.2f} {{euros€}}
=====================

"""

#*formato 7
#*puedes poner condciones para que se muestre es un valor
print(ficha)
numero = 32
print(f" ¿numero es par? {'verdadero'if numero%2==0 else 'falso'}")

print(f"Valoraciones: {'Alto' if numero > 50 else 'Medio' if numero>25 else 'Bajo'}")