"""Escribe un programa que le pida al usuario su sueldo anual (lógicamente puede ser
un número con decimales) y le informe que porcentaje de retención le corresponde, el
importe de la misma y el importe neto restante que cobrará."""


saldo = float(input("Intrduce tu sueldo: "))

if saldo > 0 and saldo < 12450:
    saldoPor = saldo * 0.19
    print(f"el porcentaje de retencion por el sueldo {round(saldo,2)} es del 19% entonces el total es: {round(saldoPor,2)}")
if saldo >= 12450 and saldo < 20200:
    saldoPor = saldo * 0.24
    print(f"el porcentaje de retencion por el sueldo {round(saldo, 2)} es del 24% entonces el total es: {round(saldoPor, 2)}")
if saldo >= 20200 and saldo < 35200:
    saldoPor = saldo * 0.30
    print(f"el porcentaje de retencion por el sueldo {round(saldo, 2)} es del 30% entonces el total es: {round(saldoPor, 2)}")
if saldo >= 35200 and saldo < 60000:
    saldoPor = saldo * 0.37
    print(f"el porcentaje de retencion por el sueldo {round(saldo, 2)} es del 37% entonces el total es: {round(saldoPor, 2)}")

if saldo >= 60000 and saldo < 300000:
    saldoPor = saldo * 0.45
    print(f"el porcentaje de retencion por el sueldo {round(saldo, 2)} es del 45% entonces el total es: {round(saldoPor, 2)}")
if saldo > 300000:
    saldoPor = saldo * 0.47
    print(f"el porcentaje de retencion por el sueldo {round(saldo, 2)}💶 es del 47% entonces el total es: {round(saldoPor, 2)}💶")