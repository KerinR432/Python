"""1. Escribir un programa que pida un número por teclado y calcule su factorial. Como
sabes, la factorial de un número se calcula multiplicando ese número por los
sucesivos factores que obtenemos restando uno hasta llegar a la unidad. Por ejemplo,
el factorial de 6 (que se representa así 6!) sería este:
6! = 6*5*4*3*2*1 = 720"""

facotorial = int(input("Introduce el numero factorial\n"))
#*vamos a guarda el fatorial que leugo multiplicaremos
rsdo = facotorial
#*de aqui sacaremos el factorial multiplicando el numero -1 * el resultado
for i in range(1,facotorial-1):
    rsdo+= rsdo*i

print(rsdo)