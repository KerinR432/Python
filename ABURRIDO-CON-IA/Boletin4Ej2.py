import time
from datetime import datetime

# ── Paleta visual "Fibonacci Oracle" ──────────────────────────────────────────
CYAN = "\033[96m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
ROJO = "\033[91m"
MAGENTA = "\033[95m"
BLANCO = "\033[97m"
RESET = "\033[0m"
NEGRITA = "\033[1m"
DIM = "\033[2m"
INVERT = "\033[7m"


def efecto_generacion():
    print(f"\n{MAGENTA}╭{'─' * 78}╮{RESET}")
    print(
        f"{MAGENTA}│{RESET}     {INVERT} INICIANDO SECUENCIA FIBONACCI – CONEXIÓN CÓSMICA {RESET}     {MAGENTA}│{RESET}")
    print(f"{MAGENTA}╰{'─' * 78}╯{RESET}\n")

    etapas = [
        "Sintonizando proporción áurea...",
        "Desplegando espiral dorada...",
        "Calculando resonancia numérica...",
        "Estabilizando secuencia infinita..."
    ]

    for etapa in etapas:
        print(f"{CYAN}→ {etapa}", end="", flush=True)
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.18)
        print(f" {VERDE}OK{RESET}")
    print()


def mostrar_fibonacci_epico(n, secuencia):
    ahora = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")

    # Preparamos la línea de números con formato bonito
    numeros_str = []
    for i, num in enumerate(secuencia):
        color = AMARILLO if i < 2 else VERDE if i < 6 else CYAN
        numeros_str.append(f"{color}{NEGRITA}{num:,}{RESET}")

    linea_numeros = "  →  ".join(numeros_str)

    print(f"""
{MAGENTA}╔{'═' * 90}╗{RESET}
{MAGENTA}║{RESET}              {NEGRITA}{BLANCO}ORÁCULO DE FIBONACCI – NIVEL 7 – SECUENCIA ACTIVADA{RESET}              {MAGENTA}║{RESET}
{MAGENTA}╠{'═' * 90}╣{RESET}
{MAGENTA}║{RESET}  Solicitud procesada: {CYAN}{n} términos{RESET}                                              {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Fecha de invocación: {DIM}{ahora}{RESET}                                         {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Proporción áurea aproximada: {AMARILLO}1.6180339887…{RESET}                                 {MAGENTA}║{RESET}
{MAGENTA}╠{'─' * 90}╣{RESET}
{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                   {VERDE}LA SECUENCIA CÓSMICA HA SIDO REVELADA{RESET}                    {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  {linea_numeros}  {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}
{MAGENTA}╠{'─' * 90}╣{RESET}
{MAGENTA}║{RESET}  {DIM}« La naturaleza está escrita en el lenguaje de las matemáticas »{RESET}           {MAGENTA}║{RESET}
{MAGENTA}║{RESET}     – Galileo Galilei                                                          {MAGENTA}║{RESET}
{MAGENTA}╚{'═' * 90}╝{RESET}

{VERDE}{NEGRITA}       ¡Has despertado la espiral infinita, viajero del código! ✨{RESET}
{DIM}       Sistema Fibonacci Oracle vφ – Precisión cuántica simulada{RESET}
""")


# ── Programa principal ─────────────────────────────────────────────────────────
print(f"\n{MAGENTA}{'═' * 100}{RESET}")
print(f"   {NEGRITA}{CYAN}FIBONACCI ORACLE TERMINAL  φ.∞  –  Edición Madrid 2026{RESET}   ")
print(f"{MAGENTA}{'═' * 100}{RESET}\n")

while True:
    try:
        n = int(input(f"{CYAN}¿Cuántos términos de la sucesión deseas invocar? → {RESET}"))
        if n < 0:
            print(f"{ROJO}No se puede invocar una cantidad negativa de términos.{RESET}\n")
            continue
        if n == 0:
            print(f"{AMARILLO}0 términos = secuencia vacía. Nada que mostrar.{RESET}\n")
            continue
        break
    except ValueError:
        print(f"{ROJO}Introduce un número entero válido, por favor.{RESET}\n")

# Generación de la secuencia
efecto_generacion()

if n == 1:
    secuencia = [0]
elif n == 2:
    secuencia = [0, 1]
else:
    secuencia = [0, 1]
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
        secuencia.append(b)

mostrar_fibonacci_epico(n, secuencia)