from datetime import date, time, datetime, timedelta

hoy = date.today()
print(hoy)

ahora = datetime.now()
print(ahora)

compleayos = date(1968, 10, 8)
citaMedica = datetime(2025,12,15,17,15)
despertador = time(6,15)
print(compleayos)
print(citaMedica)
print(despertador)

#* es la manera de formatear el objeto horas con el '-' delante no pasa ningún cero para completar
formateando1 = ahora.strftime("%H:%-M")
print(formateando1)

#* el 'y' minusculas pone el año en 2 cifras si es 'Y' pone las 4 cifras
formateando2 = ahora.strftime("%d-%m-%Y || %H:%M:%S")
print(formateando2)
#* tanto 'a' que devuelve dia como 'b' devuelve los nombre en 3 cifras, en mayusculas muestra completo
#* con la 'H' formato 24 horas, con el 'I' formato de 12 horas
#* Y el 'p' indica si es AM o PM
formateando2 = ahora.strftime("%a-%d-%B-%y || %I:%M:%S %p")
print(formateando2)
#* día de semana en número, tomando en cuenta que empieza en 'domingo'
#* el mayusculas de 'W' cuantas semanas han pasado en el año en la inglesa y la 'U'en la europea
#* el 'j' el número del día del año
formateando2 = ahora.strftime(" (%w) (%U) %a-%d-%B-%y (%j) || %I:%M:%S %p")
print(formateando2)
#* formateo automático de la hora local
formateando3 = ahora.strftime("%c")
print(formateando3)
#* el 'x' y 'X' nos devuelve fecha y letras formatos locales
formateando3 = ahora.strftime("%x")
print(formateando3)
formateando3 = ahora.strftime("%X")
print(formateando3)

cadena = "01-03-2025 14:30"

fecha = datetime.strptime(cadena,"%d-%m-%Y %H:%M")
print(fecha)

print(fecha.hour)
print(fecha.day)

#* Comparar Dias
if ahora > citaMedica:
    print("la fecha del año es posterior a tu cumple")

else:
    print("No es posterior a tu cita medica")

print(ahora)
#* Para sumar dias o tiempo que quieres sumar o restar
nuevaFecha = ahora + timedelta(days=10,hours=2,weeks=1)
print(nuevaFecha)
