import time
from datetime import datetime

# ── Colores estilo "Cyber Sum Terminal" ───────────────────────────────────────
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


def efecto_analisis_digitos():
    print(f"\n{MAGENTA}╭{'─' * 78}╮{RESET}")
    print(f"{MAGENTA}│{RESET}   {INVERT} INICIANDO ANÁLISIS PAR / IMPAR – MODO CUÁNTICO {RESET}   {MAGENTA}│{RESET}")
    print(f"{MAGENTA}╰{'─' * 78}╯{RESET}\n")

    pasos = ["Extrayendo dígitos...", "Clasificando paridad...", "Sumando planos pares...", "Sumando planos impares..."]
    for paso in pasos:
        print(f"{CYAN}→ {paso}", end="", flush=True)
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.15)
        print(f" {VERDE}OK{RESET}")
    print()


def suma_pares_impares(numero: int) -> tuple[int, int]:
    """Devuelve (suma_pares, suma_impares)"""
    if numero == 0:
        return 0, 0

    # Trabajamos con valor absoluto por si es negativo
    n = abs(numero)
    suma_par = 0
    suma_impar = 0

    while n > 0:
        digito = n % 10
        if digito % 2 == 0:
            suma_par += digito
        else:
            suma_impar += digito
        n //= 10

    return suma_par, suma_impar


def mostrar_resultado_epico(numero: int, suma_par: int, suma_impar: int):
    ahora = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
    str_num = str(numero)

    # Construimos visualización de dígitos con colores
    digitos_coloreados = []
    for d in str_num:
        dig = int(d)
        color = VERDE if dig % 2 == 0 else ROJO
        digitos_coloreados.append(f"{color}{NEGRITA}{d}{RESET}")

    digitos_str = "  ".join(digitos_coloreados)

    print(f"""
{MAGENTA}╔{'═' * 90}╗{RESET}
{MAGENTA}║{RESET}             {NEGRITA}{BLANCO}ANÁLISIS PAR-IMPAR CUÁNTICO – RESULTADOS FINALES{RESET}             {MAGENTA}║{RESET}
{MAGENTA}╠{'═' * 90}╣{RESET}
{MAGENTA}║{RESET}  Fecha análisis: {DIM}{ahora}{RESET:<66} {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Número procesado: {CYAN}{NEGRITA}{numero}{RESET} {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Dígitos descompuestos: {digitos_str} {MAGENTA}║{RESET}
{MAGENTA}╠{'─' * 90}╣{RESET}
{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}
{MAGENTA}║{RESET}    {'PARIDAD':^38}    {'SUMA':^20}                                         {MAGENTA}║{RESET}
{MAGENTA}║{RESET}    {'─' * 38}    {'─' * 20}                                         {MAGENTA}║{RESET}
{MAGENTA}║{RESET}    {'PARES':<38}{VERDE}{NEGRITA}{suma_par:>20}{RESET} {MAGENTA}║{RESET}
{MAGENTA}║{RESET}    {'IMPARES':<38}{ROJO}{NEGRITA}{suma_impar:>20}{RESET} {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}
{MAGENTA}╠{'─' * 90}╣{RESET}
{MAGENTA}║{RESET}  {DIM}« La realidad numérica ha sido diseccionada en sus componentes fundamentales »{RESET} {MAGENTA}║{RESET}
{MAGENTA}╚{'═' * 90}╝{RESET}

{VERDE}{NEGRITA}       ¡Análisis completado con precisión absoluta, Kerin! ⚛️{RESET}
{DIM}       Sistema Par-Impar Quantum Analyzer v9 – Madrid Sector{RESET}
""")


# ── Programa principal ─────────────────────────────────────────────────────────
print(f"\n{MAGENTA}{'═' * 100}{RESET}")
print(f"   {NEGRITA}{CYAN}PAR-IMPAR QUANTUM ANALYZER v9  –  Disección Numérica Avanzada{RESET}   ")
print(f"{MAGENTA}{'═' * 100}{RESET}\n")

while True:
    try:
        entrada = input(f"{CYAN}Introduce el número a analizar → {RESET}").strip()
        numero = int(entrada)
        break
    except ValueError:
        print(f"{ROJO}→ Introduce un número entero válido por favor.{RESET}\n")

efecto_analisis_digitos()

suma_par, suma_impar = suma_pares_impares(numero)

mostrar_resultado_epico(numero, suma_par, suma_impar)

# Preguntamos si continuar
continuar = input(f"\n{CYAN}¿Analizar otro número? (s/n) → {RESET}").strip().lower()
if continuar in ('s', 'si', 'y', 'yes'):
    print("\n" * 2 + "Reiniciando ciclo de análisis...\n")
    # Aquí podrías poner un bucle while True si quieres varios análisis
else:
    print(f"\n{DIM}Cerrando conexión con el Quantum Analyzer. ¡Hasta la próxima, Kerin!{RESET}\n")