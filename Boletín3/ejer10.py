""" 10. Escribe un programa que valide si un NIF español introducido por teclado es correcto.
La longitud exacta de la cadena ha de ser de 9 caractéres✅. Los ocho primeros han de
ser números comprendidos entre el 0 y el 9 y el último una letra que puede estar
escrita en mayúsculas o minúsculas."""




dni = input("Introduce tu DNI\n")

if len(dni) ==9:
    print("Bien primera seguridad cumplida")
else:
    print("Error❌")

canDigito = sum(c.isdigit() for c in dni) #Lo saque de chatgpt pero entiendo que recorre toda la cadena dijiendo cuales
#son digitos y luego suma todas esas veces.
if canDigito == 8:
    print("Bien has pasado el segundo punto de seguridad")
else:
    print("Error❌")