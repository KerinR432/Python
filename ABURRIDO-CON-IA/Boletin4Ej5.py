import time
from datetime import datetime

# ── Paleta visual "Palíndromo Oracle" ─────────────────────────────────────────
CYAN     = "\033[96m"
VERDE    = "\033[92m"
AMARILLO = "\033[93m"
ROJO     = "\033[91m"
MAGENTA  = "\033[95m"
BLANCO   = "\033[97m"
RESET    = "\033[0m"
NEGRITA  = "\033[1m"
DIM      = "\033[2m"
INVERT   = "\033[7m"


def efecto_escaneo_simetria():
    print(f"\n{MAGENTA}╭{'─'*78}╮{RESET}")
    print(f"{MAGENTA}│{RESET}     {INVERT} INICIANDO ANÁLISIS DE SIMETRÍA ESPEJO {RESET}     {MAGENTA}│{RESET}")
    print(f"{MAGENTA}╰{'─'*78}╯{RESET}\n")

    pasos = ["Leyendo secuencia...", "Invirtiendo realidad...", "Comparando ejes...", "Determinación de simetría..."]
    for paso in pasos:
        print(f"{CYAN}→ {paso}", end="", flush=True)
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.15)
        print(f" {VERDE}OK{RESET}")
    print()


def es_capicua(texto: str) -> bool:
    # Solo dígitos (ignoramos cualquier cosa que no sea número)
    digitos = ''.join(c for c in texto if c.isdigit())
    if not digitos:
        return False
    return digitos == digitos[::-1]


def mostrar_resultado_epico(original: str, digitos: str, es_capicua: bool):
    ahora = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
    invertido = digitos[::-1]

    if es_capicua:
        color_resultado = VERDE
        titulo = "SIMETRÍA PERFECTA DETECTADA"
        icono = "✓"
        mensaje = "ESPEJO CÓSMICO CONFIRMADO"
    else:
        color_resultado = ROJO
        titulo = "SIMETRÍA ROTA"
        icono = "✗"
        mensaje = "NO HAY ESPEJO PERFECTO"

    print(f"""
{color_resultado}╔{'═'*86}╗{RESET}
{color_resultado}║{RESET}              {NEGRITA}{BLANCO}{titulo}{RESET}              {color_resultado}║{RESET}
{color_resultado}╠{'═'*86}╣{RESET}
{color_resultado}║{RESET}  Fecha análisis: {DIM}{ahora}{RESET:<62} {color_resultado}║{RESET}
{color_resultado}║{RESET}  Secuencia original: {CYAN}{NEGRITA}{original}{RESET} {color_resultado}║{RESET}
{color_resultado}║{RESET}  Dígitos analizados: {AMARILLO}{digitos}{RESET} {color_resultado}║{RESET}
{color_resultado}╠{'─'*86}╣{RESET}
{color_resultado}║{RESET}                                                                              {color_resultado}║{RESET}
{color_resultado}║{RESET}                   {NEGRITA}{color_resultado}{icono}  {mensaje}  {icono}{RESET}                   {color_resultado}║{RESET}
{color_resultado}║{RESET}                                                                              {color_resultado}║{RESET}
{color_resultado}║{RESET}        {original}  {INVERT} ⇄ {RESET}  {invertido}        {color_resultado}║{RESET}
{color_resultado}║{RESET}                                                                              {color_resultado}║{RESET}
{color_resultado}╚{'═'*86}╝{RESET}

{DIM}    Palíndromo Oracle v∞ • Simetría axial verificada con precisión cuántica{RESET}
""")


# ── Programa principal ─────────────────────────────────────────────────────────
print(f"\n{MAGENTA}{'═'*100}{RESET}")
print(f"   {NEGRITA}{CYAN}PALÍNDROMO ORACLE TERMINAL  ∞  –  Detector de Espejos Numéricos{RESET}   ")
print(f"{MAGENTA}{'═'*100}{RESET}\n")

while True:
    entrada = input(f"{CYAN}Introduce un número (o secuencia) para analizar simetría → {RESET}").strip()

    if not entrada:
        print(f"{AMARILLO}→ No has introducido nada. Inténtalo de nuevo.{RESET}\n")
        continue

    efecto_escaneo_simetria()

    digitos = ''.join(c for c in entrada if c.isdigit())
    if not digitos:
        print(f"{ROJO}No se encontraron dígitos válidos en la entrada.{RESET}\n")
        continue

    capicua = es_capicua(entrada)

    mostrar_resultado_epico(entrada, digitos, capicua)

    # Preguntamos si quiere continuar
    continuar = input(f"\n{CYAN}¿Analizar otro número? (s/n) → {RESET}").strip().lower()
    if continuar not in ('s', 'si', 'y', 'yes'):
        print(f"\n{DIM}Cerrando conexión con el Oráculo de Simetría. ¡Hasta la próxima!{RESET}\n")
        break