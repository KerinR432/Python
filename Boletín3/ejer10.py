""" 10. Escribe un programa que valide si un NIF español introducido por teclado es correcto.
La longitud exacta de la cadena ha de ser de 9 caractéres✅. Los ocho primeros han de
ser números comprendidos entre el 0 y el 9 y el último una letra que puede estar
escrita en mayúsculas o minúsculas."""




for i in DNITem:
    if DNITem[i]>1 and DNITem[i] <= 9:
        print("Bien el DNI esta bien")
    else:
        print("No tiene numero o ha fallado el programa")