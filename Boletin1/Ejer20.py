# pedimos por teclado
num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))
num3 = int(input("Introduce un numero: "))

#ordenar
if num1>num2:
    if num2>num3:
        print(f"{num3};{num2};{num1}")
    else:
        print(f"{num2};{num3};{num1}")
if num2>num3:
    if num1<num3:
        print(f"{num1};{num3};{num2}")
    else:
        print(f"{num3};{num1};{num2}")
if num3>num2:
    if num1<num2:
        print(f"{num1};{num2};{num3}")
    else:
        print(f"{num2};{num1};{num3}")