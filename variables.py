edad = 56  #variable numerica

print(edad)

texto = "Cincuenta seis" #variable de tipo texto
print(texto)

precio = 54.4 #variable decimal
acertado = True #variable booleana

print(precio)
print(acertado)

MESES_DEL_ANNO = 12 #no existen contaste solo es una indicación de que no teiene que cambiar este codigo

#OPERADORES ARRITMETICOS
print("--------------------")
print(5//2) #el cociente
print(5%2) #resto
print(5/2) #division

nuevo = precio * (5 + edad) #Prioridad de aritmetica
print(nuevo)
print(1/33) #decimales

print("-------------------------")
#CADENAS
texto = "Hola"
#texto = texto + " " + "Mundo"
print(texto)
print(texto + "Mundo")
print(texto, "Mundo")
curso = 2
ciclo = "DAW"
print(texto, "Mundo", end= " ",sep="-") # el sustituye por cualquier cosa el salto de linea SEP separa entre elemento
print("Bienvenidos todos los de",curso,ciclo) #el print puede componer todo tipo de variable

print("-------------------------")
#RECORGER DATOS DEL TECLADO

#edad1 = input("Introduce tu edad: ") #es un input String
#if edad1 < 18:
#        print("Eres menor de edad")
#else :
#    print("Eres mayor de edad")
#print(edad1)

edad2 = int(input("Introduce tu edad: ")) #es un input cambia el valor a int
if int(edad2) < 18: #castea el valor y cambia el valor a int
        print("Eres menor de edad")
else :
    print("Eres mayor de edad")


sueldo = float(input("Dime tu sueldo: "))
if sueldo > 18000.56:
    print("Debes de ser Rico")
else :
    print("No se si tienes para un piso")

print("Fin del programa")
# el and or y not se escribe con palabras y no pasa nada

#BUCLES

for n in range(0,10,2): # un bluce for, asi se forma y una 3 es para ir saltando de ese numero a numero
    print(n)
print("Fin del programa")

for n in range (10,0,-1): # para decrecer el for
    print(n)

for c in "Hola Mundo":
    print(c)

mayor = max(25.6,55,67.6,1)
print(max)
menor = min(25.6,55,67.6,1)
print(menor)