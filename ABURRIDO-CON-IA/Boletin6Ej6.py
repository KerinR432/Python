import re
from datetime import datetime
import time  # para pequeños "efectos" de carga

# ── Colores ANSI (funcionan en terminales modernas: VS Code, Windows Terminal, iTerm, etc.)
CYAN     = "\033[96m"
VERDE    = "\033[92m"
AMARILLO = "\033[93m"
ROJO     = "\033[91m"
MAGENTA  = "\033[95m"
RESET    = "\033[0m"
NEGRITA  = "\033[1m"
DIM      = "\033[2m"
BLANCO   = "\033[97m"

# Patrón correcto: XX00-xxX-00
#   • 2 mayúsculas
#   • 2 dígitos
#   • guión
#   • 2 minúsculas
#   • 1 mayúscula
#   • guión
#   • 2 dígitos
PATRON_CLAVE = r'^[A-Z]{2}\d{2}-[a-z]{2}[A-Z]-\d{2}$'


def mostrar_exito(clave):
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"""
{MAGENTA}╔{'═'*78}╗{RESET}
{MAGENTA}║{RESET}  {'ACCESS GRANTED – CLAVE VÁLIDA':^76}  {MAGENTA}║{RESET}
{MAGENTA}╠{'═'*78}╣{RESET}
{MAGENTA}║{RESET}  Clave: {VERDE}{NEGRITA}{clave:^64}{RESET}  {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Formato: {CYAN}XX00-xxX-00{RESET} → {VERDE}100% correcto{RESET}                     {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Verificado: {DIM}{ahora}{RESET}                                 {MAGENTA}║{RESET}
{MAGENTA}╠{'─'*78}╣{RESET}
{MAGENTA}║{RESET}  {VERDE}✓ Sistema desbloqueado. Bienvenido al núcleo seguro. ✓{RESET}           {MAGENTA}║{RESET}
{MAGENTA}╚{'═'*78}╝{RESET}

       {VERDE}PROTOCOLO DE SEGURIDAD NIVEL 7 – AUTORIZACIÓN CONFIRMADA{RESET}
       {DIM}Vault 29 – Madrid Sector – Acceso concedido{RESET}
""")


def mostrar_error(clave, motivo=""):
    print(f"""
{ROJO}╔{'═'*78}╗{RESET}
{ROJO}║{RESET}  {'ACCESS DENIED – CLAVE INVÁLIDA':^76}  {ROJO}║{RESET}
{ROJO}╠{'═'*78}╣{RESET}
{ROJO}║{RESET}  Introducido: {AMARILLO}{clave:^58}{RESET}  {ROJO}║{RESET}
{ROJO}║{RESET}  Motivo:     {DIM}{motivo or 'No cumple el formato exacto XX00-xxX-00'}{RESET:<58}  {ROJO}║{RESET}
{ROJO}╠{'─'*78}╣{RESET}
{ROJO}║{RESET}  Formato esperado exactamente:{RESET}                                       {ROJO}║{RESET}
{ROJO}║{RESET}      {CYAN}AB12-xyZ-75{RESET}   o   {CYAN}XY99-abC-00{RESET}                                     {ROJO}║{RESET}
{ROJO}║{RESET}      → 2 mayúsculas • 2 dígitos • - • 2 minúsculas • 1 mayúscula • - • 2 dígitos  {ROJO}║{RESET}
{ROJO}╚{'═'*78}╝{RESET}

       {ROJO}INTENTO RECHAZADO – Vuelve a intentarlo{RESET}
""")


def efecto_carga():
    print(f"{CYAN}Validando clave", end="", flush=True)
    for _ in range(5):
        time.sleep(0.15)
        print(".", end="", flush=True)
    print(f"{RESET}")


# ── Programa principal ─────────────────────────────────────────────────────────
print("\n" * 2)
print(f"{MAGENTA}{'═'*90}{RESET}")
print(f"   {NEGRITA}VAULT ACCESS – VALIDACIÓN CLAVE SEGURA  XX00-xxX-00   {RESET}")
print(f"   {DIM}Nivel de seguridad: 7 – Solo personal autorizado{RESET}")
print(f"{MAGENTA}{'═'*90}{RESET}\n")

while True:
    clave = input(f"{CYAN}Introduce la clave de acceso → {RESET}").strip()

    if not clave:
        print(f"{AMARILLO}→ Campo vacío. Introduce una clave.{RESET}\n")
        continue

    efecto_carga()

    if re.match(PATRON_CLAVE, clave):
        mostrar_exito(clave)
        break
    else:
        # Diagnóstico rápido (opcional – mejora UX)
        motivo = ""
        if len(clave) != 12:
            motivo = f"Longitud incorrecta ({len(clave)} caracteres en lugar de 12)"
        elif not re.match(r'^[A-Z]{2}', clave):
            motivo = "Los dos primeros caracteres deben ser mayúsculas"
        elif not re.match(r'^[A-Z]{2}\d{2}', clave):
            motivo = "Después de las mayúsculas deben venir 2 dígitos"
        elif clave[4] != '-':
            motivo = "Falta el primer guión en posición 5"
        elif not re.match(r'^[A-Z]{2}\d{2}-[a-z]{2}', clave):
            motivo = "Después del primer guión deben venir 2 minúsculas"
        elif clave[9] != '-':
            motivo = "Falta el segundo guión en posición 10"
        elif not re.match(r'^[A-Z]{2}\d{2}-[a-z]{2}[A-Z]-\d{2}$', clave):
            motivo = "El penúltimo carácter debe ser mayúscula y los últimos 2 dígitos"

        mostrar_error(clave, motivo)