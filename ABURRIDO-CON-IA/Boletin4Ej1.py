import time
from datetime import datetime

# ── PALETA CYBER-MATEMÁTICA (Madrid Edition) ───────────────────────────────────
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


def efecto_calculo_intenso():
    print(f"\n{MAGENTA}╔{'═' * 72}╗{RESET}")
    print(
        f"{MAGENTA}║{RESET}       {INVERT} INICIANDO CÁLCULO FACTORIAL ULTRA-DIMENSIONAL {RESET}       {MAGENTA}║{RESET}")
    print(f"{MAGENTA}╚{'═' * 72}╝{RESET}\n")

    pasos = ["ANALIZANDO NÚMERO", "DESPLEGANDO SUCESIÓN", "MULTIPLICANDO DIMENSIONES", "COMPRIMIENDO RESULTADO",
             "ESTABILIZANDO REALIDAD"]
    for paso in pasos:
        print(f"{CYAN}» {paso}...", end="", flush=True)
        time.sleep(0.4)
        for _ in range(3):
            print(f"{AMARILLO}.", end="", flush=True)
            time.sleep(0.2)
        print(f"{VERDE} OK{RESET}")


def calcular_factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1

    factorial = 1
    operacion = []
    for i in range(n, 0, -1):
        factorial *= i
        operacion.append(str(i))

    return factorial, " × ".join(operacion)


def mostrar_factorial_epico(n, resultado, operacion_str):
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Formateamos el número grande con separadores de miles
    resultado_str = f"{resultado:,}".replace(",", ".")

    print(f"""
{MAGENTA}╔{'═' * 82}╗{RESET}
{MAGENTA}║{RESET}                   {NEGRITA}{BLANCO}¡FACTORIAL CALCULADO CON ÉXITO!{RESET}                   {MAGENTA}║{RESET}
{MAGENTA}╠{'═' * 82}╣{RESET}
{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}
{MAGENTA}║{RESET}       Número introducido → {AMARILLO}{NEGRITA}{n}{RESET}                                                  {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}
{MAGENTA}║{RESET}       Operación completa → {CYAN}{n}! = {operacion_str}{RESET}                     {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}
{MAGENTA}║{RESET}       {INVERT}{BLANCO} RESULTADO FINAL → {resultado_str} {RESET}                            {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}
{MAGENTA}║{RESET}       Cálculo realizado el: {DIM}{ahora}{RESET}                               {MAGENTA}║{RESET}
{MAGENTA}║{RESET}       Ubicación: {VERDE}Madrid, España{RESET}                                           {MAGENTA}║{RESET}
{MAGENTA}╚{'═' * 82}╝{RESET}

{VERDE}{NEGRITA}       ¡EL UNIVERSO MATEMÁTICO TIEMBLA ANTE TU PODER, KERIN! ✨{RESET}
{DIM}       Sistema de cálculo cuántico simulado • Precisión absoluta garantizada{RESET}
""")


# ── MAIN ÉPICO ────────────────────────────────────────────────────────────────
print(f"\n{MAGENTA}{'═' * 90}{RESET}")
print(f"{CYAN}{NEGRITA}                FACTORIAL CALCULATOR 9000-X • EDICIÓN MADRILEÑA{RESET}")
print(f"{MAGENTA}{'═' * 90}{RESET}\n")

while True:
    try:
        entrada = input(f"{CYAN}Introduce un número entero positivo → {RESET}")
        numero = int(entrada)

        if numero < 0:
            print(f"{ROJO}¡Error! El factorial no está definido para números negativos.{RESET}\n")
            continue
        break

    except ValueError:
        print(f"{ROJO}¡Por favor, introduce un número entero válido!{RESET}\n")

efecto_calculo_intenso()

resultado, operacion = calcular_factorial(numero)
mostrar_factorial_epico(numero, resultado, operacion)

# Bonus: si es un número muy grande, mensaje especial
if numero >= 15:
    print(f"{AMARILLO}{NEGRITA}       ¡ADVERTENCIA! Has calculado un factorial extremadamente grande.{RESET}")
    print(f"{DIM}       Este número tiene {len(str(resultado))} dígitos. ¡Eres un monstruo matemático! 😈{RESET}")