import re
from datetime import datetime
import time

# ── Colores ANSI (funcionan en terminales modernas) ────────────────────────────
CYAN = "\033[96m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
ROJO = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
NEGRITA = "\033[1m"
DIM = "\033[2m"
BLANCO = "\033[97m"

# Patrón: solo dígitos, entre 4 y 8 inclusive
PATRON_NUMERO = r'^\d{4,8}$'


def efecto_escaneo():
    print(f"{CYAN}ESCANEANDO SECUENCIA", end="", flush=True)
    for _ in range(5):
        time.sleep(0.11)
        print(".", end="", flush=True)
    print(f"{RESET}")


def mostrar_exito(numero):
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    longitud = len(numero)

    print(f"""
{MAGENTA}╔{'═' * 78}╗{RESET}
{MAGENTA}║{RESET}  {'CÓDIGO ACEPTADO – SECUENCIA VÁLIDA':^76}  {MAGENTA}║{RESET}
{MAGENTA}╠{'═' * 78}╣{RESET}
{MAGENTA}║{RESET}  Secuencia: {VERDE}{NEGRITA}{numero.center(60)}{RESET}  {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Longitud:  {AMARILLO}{longitud} dígitos{RESET}  (rango aceptado: 4–8)          {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Validado:  {DIM}{ahora}{RESET}                                 {MAGENTA}║{RESET}
{MAGENTA}╠{'─' * 78}╣{RESET}
{MAGENTA}║{RESET}  {VERDE}✓ Integridad confirmada – Acceso nivel 4 autorizado ✓{RESET}         {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Protocolo:     {VERDE}NUMERIC_LOCK_7.1{RESET} – Secure Hash Match       {MAGENTA}║{RESET}
{MAGENTA}╚{'═' * 78}╝{RESET}

       {VERDE}NODO AUTORIZADO – BIENVENIDO AL NÚCLEO{RESET}
       {DIM}Sector Madrid – Protocolo activo – Encriptación activa{RESET}
""")


def mostrar_error(numero, motivo=""):
    print(f"""
{ROJO}╔{'═' * 78}╗{RESET}
{ROJO}║{RESET}  {'ACCESO DENEGADO – SECUENCIA INVÁLIDA':^76}  {ROJO}║{RESET}
{ROJO}╠{'═' * 78}╣{RESET}
{ROJO}║{RESET}  Introducido: {AMARILLO}{numero or '(vacío)':^58}{RESET}  {ROJO}║{RESET}
{ROJO}║{RESET}  Motivo:     {DIM}{motivo or 'Longitud fuera de rango (4–8 dígitos)'}{RESET:<58}  {ROJO}║{RESET}
{ROJO}╠{'─' * 78}╣{RESET}
{ROJO}║{RESET}  Requisitos exactos:{RESET}                                               {ROJO}║{RESET}
{ROJO}║{RESET}     • Solo dígitos (0-9){RESET}                                            {ROJO}║{RESET}
{ROJO}║{RESET}     • Mínimo 4 dígitos{RESET}                                             {ROJO}║{RESET}
{ROJO}║{RESET}     • Máximo 8 dígitos{RESET}                                             {ROJO}║{RESET}
{ROJO}║{RESET}     Ejemplos válidos:  1234   56789   90123456{RESET}                    {ROJO}║{RESET}
{ROJO}╚{'═' * 78}╝{RESET}

       {ROJO}INTENTO RECHAZADO – CORRIJA LA SECUENCIA{RESET}
""")


# ── Programa principal ─────────────────────────────────────────────────────────
print("\n" * 2)
print(f"{MAGENTA}{'═' * 90}{RESET}")
print(f"   {NEGRITA}NUMERIC SEQUENCE VALIDATOR – SECURE ACCESS NODE v4.2{RESET}   ")
print(f"   {DIM}Solo dígitos – Longitud permitida: 4 a 8 caracteres{RESET}")
print(f"{MAGENTA}{'═' * 90}{RESET}\n")

while True:
    entrada = input(f"{CYAN}Introduce la secuencia numérica → {RESET}").strip()

    if not entrada:
        print(f"{AMARILLO}→ Campo vacío. Introduce una secuencia.{RESET}\n")
        continue

    efecto_escaneo()

    # Quitamos cualquier cosa que no sea dígito para diagnóstico
    solo_digitos = re.sub(r'\D', '', entrada)

    if re.match(PATRON_NUMERO, entrada):
        mostrar_exito(entrada)
        break
    else:
        motivo = ""
        if len(solo_digitos) < 4:
            motivo = f"Longitud insuficiente ({len(solo_digitos)} dígitos)"
        elif len(solo_digitos) > 8:
            motivo = f"Longitud excesiva ({len(solo_digitos)} dígitos)"
        elif len(solo_digitos) != len(entrada):
            motivo = "Contiene caracteres no numéricos"
        else:
            motivo = "Secuencia no válida"

        mostrar_error(entrada, motivo)