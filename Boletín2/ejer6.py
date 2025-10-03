"""6. Modifica el ejercicio anterior para que la nota del boletín se redondee matemáticamente
si es superior a 5 pero se trunquen los decimales si es inferior a 5"""

# Pedimos por teclado
notaT = float(input("Intorduce la nota de los trabajos en clases: \n"))
notaJ = float(input("Introduce la nota de los trabajos practicos: \n"))
notaE = float(input("Introduce la nota de los examenes:\n"))

# Creamos variables que no varian
cincoPor = 0.05
quincePor = 0.15
ochentaPor = 0.80

# creamos la operación

rsdo = notaT * cincoPor
rsdo2 = notaJ * quincePor
rsdo3 = notaE * ochentaPor

# Mostramos el resultado
if notaT>5:
    print(f"La nota que tienes es: {notaT} y en el boletín tienes {round(rsdo,1)}" )
else:
    print(f"La nota que tienes es: {notaT} y en el boletín tiene {rsdo}" )
    if notaJ>5:
        print(f"La nota que tienes es: {notaJ} y en el boletín tienes {round(rsdo2, 1)}")
    else:
        print(f"La nota que tienes es: {notaJ} y en el boletín tiene {rsdo2}")
    if notaE>5:
        print(f"La nota que tienes es: {notaE} y en el boletín tienes {round(rsdo3, 1)}")
    else:
        print(f"La nota que tienes es: {notaE} y en el boletín tiene {rsdo3}")
print(f"tu nota final es: {round(rsdo+rsdo2+rsdo3,1)}" )
print(f"tu nota final es: {rsdo + rsdo2 + rsdo3}")