import random

num = int(input("Introduce un numero: "))
divisores =[]
divisores2 =[]
num2 = int(input("Introduce un numero: "))

def divisoresComunes(divisor,divisor2):
    for i in range(1, divisor +1):
        if(divisor % i) == 0:
            divisores.append(i)

    for i in range(1, divisor2 +1):
        if(divisor2 % i) == 0:
            divisores2.append(i)
    return divisores,divisores2
divisor1,divisor2 = divisoresComunes(num,num2)

if len(divisor1) > len(divisor2):
    for i in range(0, len(divisor2)):
        if divisor1[i] == divisor2[i]:
            print(divisor1[i])
else:
    for i in range(0, len(divisor1)):
        if divisor1[i] == divisor2[i]:
            print(divisor2[i])


