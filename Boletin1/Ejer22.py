import math
import random
"""22. Escribir un programa que genere un número primo aleatorio entre el 10.000.000 y el
50.000.000"""

#pedimos una variable
num1 = random.randint(10000000,50000000)

num2 = math.sqrt(num1)
primo = True
for i in range(2,int(num2)):
    if num1%i==0:
        primo = False


print(primo,num1)