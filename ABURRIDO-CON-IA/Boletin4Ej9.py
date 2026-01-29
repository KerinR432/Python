import time
from datetime import datetime

# ── Paleta visual "Character Scanner v∞" ──────────────────────────────────────
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


def efecto_escaneo_texto():
    print(f"\n{MAGENTA}╭{'─'*84}╮{RESET}")
    print(f"{MAGENTA}│{RESET}        {INVERT} INICIANDO ESCÁNER DE CARACTERES – MODO MATRIX {RESET}        {MAGENTA}│{RESET}")
    print(f"{MAGENTA}╰{'─'*84}╯{RESET}\n")

    pasos = [
        "Cargando flujo de texto...",
        "Inicializando patrón de búsqueda...",
        "Escaneando matriz carácter a carácter...",
        "Extrayendo coordenadas..."
    ]

    for paso in pasos:
        print(f"{CYAN}→ {paso}", end="", flush=True)
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.14)
        print(f" {VERDE}OK{RESET}")
    print()


def resaltar_coincidencias(texto: str, caracter: str, posiciones: list[int]):
    """Devuelve el texto original con las coincidencias resaltadas"""
    resultado = []
    for i, c in enumerate(texto):
        if i in posiciones:
            resultado.append(f"{AMARILLO}{NEGRITA}{c}{RESET}")
        else:
            resultado.append(f"{DIM}{c}{RESET}")
    return "".join(resultado)


def mostrar_resultado_epico(texto: str, caracter: str, posiciones: list[int]):
    ahora = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
    cantidad = len(posiciones)

    if not posiciones:
        print(f"""
{ROJO}╔{'═'*90}╗{RESET}
{ROJO}║{RESET}               {NEGRITA}{BLANCO}ESCÁNER FINALIZADO – NINGUNA COINCIDENCIA{RESET}               {ROJO}║{RESET}
{ROJO}╠{'═'*90}╣{RESET}
{ROJO}║{RESET}  Fecha escaneo: {DIM}{ahora}{RESET:<66} {ROJO}║{RESET}
{ROJO}║{RESET}  Carácter buscado: {ROJO}{NEGRITA}'{caracter}'{RESET} {ROJO}║{RESET}
{ROJO}║{RESET}  Texto analizado: {DIM}{texto[:70]}{'...' if len(texto)>70 else ''}{RESET} {ROJO}║{RESET}
{ROJO}╠{'─'*90}╣{RESET}
{ROJO}║{RESET}                                                                              {ROJO}║{RESET}
{ROJO}║{RESET}                   {ROJO}{NEGRITA}✗  PATRÓN NO DETECTADO  ✗{RESET}                   {ROJO}║{RESET}
{ROJO}║{RESET}                                                                              {ROJO}║{RESET}
{ROJO}╚{'═'*90}╝{RESET}

{DIM}    Character Scanner v∞ • No se encontraron coincidencias en la matriz{RESET}
""")
        return

    texto_resaltado = resaltar_coincidencias(texto, caracter, posiciones)
    pos_str = ", ".join(f"{AMARILLO}{p}{RESET}" for p in posiciones)

    print(f"""
{MAGENTA}╔{'═'*90}╗{RESET}
{MAGENTA}║{RESET}               {NEGRITA}{BLANCO}ESCÁNER FINALIZADO – COINCIDENCIAS DETECTADAS{RESET}               {MAGENTA}║{RESET}
{MAGENTA}╠{'═'*90}╣{RESET}
{MAGENTA}║{RESET}  Fecha escaneo: {DIM}{ahora}{RESET:<66} {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Carácter buscado: {VERDE}{NEGRITA}'{caracter}'{RESET} {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Ocurrencias totales: {AMARILLO}{NEGRITA}{cantidad}{RESET} {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Posiciones (0-based): {pos_str} {MAGENTA}║{RESET}
{MAGENTA}╠{'─'*90}╣{RESET}
{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                   {VERDE}{NEGRITA}✓  PATRÓN ENCONTRADO  ✓{RESET}                   {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Texto con coincidencias resaltadas:                                            {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  {texto_resaltado} {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}
{MAGENTA}╚{'═'*90}╝{RESET}

{VERDE}{NEGRITA}       ¡Escaneo completado con éxito, Kerin! La matriz ha hablado.{RESET}
{DIM}       Character Scanner v∞ • Coordenadas extraídas con precisión absoluta{RESET}
""")


# ── Programa principal ─────────────────────────────────────────────────────────
print(f"\n{MAGENTA}{'═'*100}{RESET}")
print(f"   {NEGRITA}{CYAN}CHARACTER SCANNER v∞  –  Matrix Text Analyzer – Madrid Sector{RESET}   ")
print(f"{MAGENTA}{'═'*100}{RESET}\n")

while True:
    texto = input(f"{CYAN}Ingresa el texto a escanear → {RESET}").strip()
    if not texto:
        print(f"{AMARILLO}→ No has introducido texto. Inténtalo de nuevo.{RESET}\n")
        continue

    buscado = input(f"{CYAN}Carácter a buscar (solo 1) → {RESET}").strip()

    if len(buscado) != 1:
        print(f"{ROJO}→ Error: Debes introducir exactamente UN carácter.{RESET}\n")
        continue

    efecto_escaneo_texto()

    # Búsqueda (ignoramos mayúsculas/minúsculas)
    texto_lower = texto.lower()
    char_lower = buscado.lower()
    posiciones = [i for i, c in enumerate(texto_lower) if c == char_lower]

    mostrar_resultado_epico(texto, char_lower, posiciones)

    # Preguntamos si continuar
    continuar = input(f"\n{CYAN}¿Escanear otro texto? (s/n) → {RESET}").strip().lower()
    if continuar not in ('s', 'si', 'y', 'yes'):
        print(f"\n{DIM}Cerrando conexión con el Character Scanner. ¡Hasta la próxima!{RESET}\n")
        break