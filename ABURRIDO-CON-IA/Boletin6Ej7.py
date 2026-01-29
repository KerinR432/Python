import re
from datetime import datetime
import time

# ── Colores ANSI (para terminales modernas) ────────────────────────────────────
CYAN     = "\033[96m"
VERDE    = "\033[92m"
AMARILLO = "\033[93m"
ROJO     = "\033[91m"
MAGENTA  = "\033[95m"
RESET    = "\033[0m"
NEGRITA  = "\033[1m"
DIM      = "\033[2m"
BLANCO   = "\033[97m"

# Patrón estricto y correcto
# 4 grupos de 4 dígitos separados por espacio + espacio + MM/YY (MM 01-12)
PATRON_TARJETA = r"^\d{4} \d{4} \d{4} \d{4} (0[1-9]|1[0-2])/\d{2}$"


def efecto_verificacion():
    print(f"{CYAN}Verificando tarjeta", end="", flush=True)
    for _ in range(6):
        time.sleep(0.12)
        print(".", end="", flush=True)
    print(f"{RESET}")


def mostrar_tarjeta_valida(tarjeta):
    ahora = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    ultimos4 = tarjeta.split()[3]
    mes, anio = tarjeta.split()[-1].split("/")

    print(f"""
{MAGENTA}╔{'═'*78}╗{RESET}
{MAGENTA}║{RESET}  {'TRANSACCIÓN AUTORIZADA – TARJETA VÁLIDA':^76}  {MAGENTA}║{RESET}
{MAGENTA}╠{'═'*78}╣{RESET}
{MAGENTA}║{RESET}  Tarjeta: {VERDE}{NEGRITA}{tarjeta[:15]}•••• •••• {ultimos4}{RESET}  {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Caducidad:     {AMARILLO}{mes}/{anio}{RESET}  (válida)                                 {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Verificado:    {DIM}{ahora}{RESET}                                 {MAGENTA}║{RESET}
{MAGENTA}╠{'─'*78}╣{RESET}
{MAGENTA}║{RESET}  {VERDE}✓ Autorización aprobada – Fondos suficientes detectados ✓{RESET}        {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Estado:        {VERDE}APROBADA{RESET} – Procesando pago seguro...          {MAGENTA}║{RESET}
{MAGENTA}╚{'═'*78}╝{RESET}

       {VERDE}SECURE PAYMENT GATEWAY – Nivel PCI DSS 4.0{RESET}
       {DIM}Terminal autorizada – Transacción encriptada AES-256{RESET}
""")


def mostrar_tarjeta_invalida(tarjeta, motivo=""):
    print(f"""
{ROJO}╔{'═'*78}╗{RESET}
{ROJO}║{RESET}  {'TRANSACCIÓN RECHAZADA – TARJETA NO VÁLIDA':^76}  {ROJO}║{RESET}
{ROJO}╠{'═'*78}╣{RESET}
{ROJO}║{RESET}  Introducido: {AMARILLO}{tarjeta:^58}{RESET}  {ROJO}║{RESET}
{ROJO}║{RESET}  Motivo:     {DIM}{motivo or 'No cumple formato o mes inválido'}{RESET:<58}  {ROJO}║{RESET}
{ROJO}╠{'─'*78}╣{RESET}
{ROJO}║{RESET}  Formato esperado exactamente:{RESET}                                       {ROJO}║{RESET}
{ROJO}║{RESET}      {CYAN}1234 5678 9012 3456 03/25{RESET}                                     {ROJO}║{RESET}
{ROJO}║{RESET}      → 16 dígitos (4 grupos de 4) • espacio • MM/YY (01-12)               {ROJO}║{RESET}
{ROJO}╚{'═'*78}╝{RESET}

       {ROJO}OPERACIÓN DENEGADA – Verifica los datos{RESET}
""")


# ── Programa principal ─────────────────────────────────────────────────────────
print("\n" * 2)
print(f"{MAGENTA}{'═'*90}{RESET}")
print(f"   {NEGRITA}SECURE CARD VALIDATOR – PCI DSS TERMINAL v3.9{RESET}   ")
print(f"   {DIM}Formato: XXXX XXXX XXXX XXXX MM/YY  (MM 01-12){RESET}")
print(f"{MAGENTA}{'═'*90}{RESET}\n")

while True:
    entrada = input(f"{CYAN}Introduce número de tarjeta + caducidad → {RESET}").strip()

    if not entrada:
        print(f"{AMARILLO}→ No has introducido nada. Inténtalo de nuevo.{RESET}\n")
        continue

    efecto_verificacion()

    if re.match(PATRON_TARJETA, entrada):
        mostrar_tarjeta_valida(entrada)
        break
    else:
        # Diagnóstico básico para mejorar UX
        motivo = ""
        partes = entrada.split()
        if len(partes) != 5:
            motivo = "Deben ser exactamente 5 partes separadas por espacio"
        elif not all(len(p) == 4 for p in partes[:4]):
            motivo = "Cada grupo numérico debe tener exactamente 4 dígitos"
        elif partes[4].count("/") != 1:
            motivo = "La caducidad debe tener formato MM/YY"
        else:
            mm, yy = partes[4].split("/")
            if not (mm.isdigit() and yy.isdigit()):
                motivo = "Mes y año deben ser numéricos"
            elif not (1 <= int(mm) <= 12):
                motivo = f"Mes inválido: {mm} (debe estar entre 01 y 12)"
            elif len(mm) != 2 or len(yy) != 2:
                motivo = "Mes y año deben tener exactamente 2 dígitos cada uno"

        mostrar_tarjeta_invalida(entrada, motivo)