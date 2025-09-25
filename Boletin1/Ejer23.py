"""23. Escribir un programa que te escriba todos los números primos que hay entre el 1 y el 100"""
#pedimos una variable

for x in range(1,101):
    primo = True
    for i in range(2,int(x**.5)+1):
        if x%i==0:
            primo = False
    if primo:
        print(x)