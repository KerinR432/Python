import random
import time
from datetime import datetime

# ── Colores para la terminal (funcionan en la mayoría de terminales modernas)
CYAN = "\033[96m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
ROJO = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
NEGRITA = "\033[1m"
DIM = "\033[2m"


def efecto_bolillero():
    print(f"\n{CYAN}{NEGRITA}┌───────────────────────────────┐{RESET}")
    print(f"{CYAN}│     BOLILLERO EN MOVIMIENTO... │{RESET}")
    print(f"{CYAN}└───────────────────────────────┘{RESET}\n")

    for _ in range(4):
        print(f"  {AMARILLO}●●●●●●●●●●●●●●●●●●●●●●●●●●{RESET}", end="\r")
        time.sleep(0.18)
        print(f"  {ROJO}●●●●●●●●●●●●●●●●●●●●●●●●●●{RESET}", end="\r")
        time.sleep(0.18)
    print(" " * 50, end="\r")  # limpia la línea


def mostrar_sorteo(numeros):
    ahora = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")

    print(f"""
{MAGENTA}╔══════════════════════════════════════════════════════════════╗{RESET}
{MAGENTA}║{RESET}             {NEGRITA}SORTEO PRIMITIVA – COMBINACIÓN GANADORA{RESET}           {MAGENTA}║{RESET}
{MAGENTA}╠══════════════════════════════════════════════════════════════╣{RESET}
{MAGENTA}║{RESET}  Fecha sorteo: {DIM}{ahora}{RESET:<42} {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                                                              {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                    {CYAN}NÚMEROS PREMIADOS{RESET}                      {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                                                              {MAGENTA}║{RESET}
""")

    # Mostramos los números en una fila con efecto "luz"
    linea_numeros = "  ".join(f"{AMARILLO}{NEGRITA}{n:2d}{RESET}" for n in numeros)
    print(f"{MAGENTA}║{RESET}               {linea_numeros}               {MAGENTA}║{RESET}")

    print(f"""
{MAGENTA}║{RESET}                                                              {MAGENTA}║{RESET}
{MAGENTA}║{RESET}         {VERDE}¡Comprueba tu boleto! Suerte en el próximo sorteo!{RESET}      {MAGENTA}║{RESET}
{MAGENTA}╚══════════════════════════════════════════════════════════════╝{RESET}

{DIM}    Sistema RNG certificado – Números generados sin repetición    {RESET}
""")


# ── Generación real ────────────────────────────────────────────────────────────
numeros = random.sample(range(1, 50), 6)
numeros.sort()  # ordenados por estética (opcional, pero queda mejor)

efecto_bolillero()
mostrar_sorteo(numeros)

print(f"\n{CYAN}Combinación final:{RESET} {', '.join(f'{n:02d}' for n in numeros)}\n")