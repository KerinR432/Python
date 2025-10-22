segundo = int(input("Introduce segundos\n"))
minuto = 0
horas = 0
dias = 0
cont = 0
segundos2 = 0


for n in range(0,segundo):
    if segundos2 <= 60:
        segundos2 +=1
    if segundos2 >=60:
        minuto +=1
        segundos2 = 0
    if minuto >=60:
        horas+=1
        minuto = 0
    if horas >=24:
        dias+=1
        horas = 0

if segundos2 > 0:
    print(f"para los {segundo} segundos han pasado: {dias} Dias con {horas} horas:{minuto} minutos")
print(f"para los {segundo} segundos han pasado: {dias} Dias con {horas} horas:{minuto} minutos:{segundos2} segundos")