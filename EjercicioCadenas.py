texto = input("Introduce un texto: ")
texto2 = " "
for c in texto:

    if c != " ":
        texto2+=c

print(texto2,end="")