import re
from datetime import datetime
import sys

# ── Colores (funcionan en la mayoría de terminales modernas) ───────────────
CYAN     = "\033[96m"
VERDE    = "\033[92m"
AMARILLO = "\033[93m"
ROJO     = "\033[91m"
MAGENTA  = "\033[95m"
RESET    = "\033[0m"
NEGRITA  = "\033[1m"
DIM      = "\033[2m"


def limpiar_texto(texto: str) -> str:
    # Quitamos signos de puntuación comunes y normalizamos espacios
    texto = re.sub(r'[^\w\sáéíóúÁÉÍÓÚñÑüÜ]', '', texto)   # solo letras, números y espacios
    texto = re.sub(r'\s+', ' ', texto.strip())            # múltiples espacios → uno solo
    return texto


def contar_palabras(texto: str) -> int:
    if not texto.strip():
        return 0
    palabras = texto.split()
    return len(palabras)


def mostrar_resultado(texto_original: str, num_palabras: int):
    ahora = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    longitud = len(texto_original)
    palabras = num_palabras

    print(f"""
{MAGENTA}╔══════════════════════════════════════════════════════════════════════════════╗{RESET}
{MAGENTA}║{RESET}                 {NEGRITA}ANÁLISIS DE TEXTO – MODO TERMINAL ÉPICO{RESET}                 {MAGENTA}║{RESET}
{MAGENTA}╠══════════════════════════════════════════════════════════════════════════════╣{RESET}
{MAGENTA}║{RESET}  Fecha análisis: {DIM}{ahora}{RESET:<50} {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Longitud total: {CYAN}{longitud:,}{RESET} caracteres {MAGENTA}║{RESET}
{MAGENTA}╠──────────────────────────────────────────────────────────────────────────────╣{RESET}
{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                   {VERDE}{NEGRITA}NÚMERO DE PALABRAS DETECTADAS{RESET}                        {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                         {AMARILLO}{NEGRITA}{palabras:^{30}}{RESET}                              {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  {DIM}« {texto_original[:60]}{"..." if len(texto_original)>60 else ""} »{RESET:<68} {MAGENTA}║{RESET}
{MAGENTA}║{RESET}                                                                              {MAGENTA}║{RESET}
{MAGENTA}╠──────────────────────────────────────────────────────────────────────────────╣{RESET}
{MAGENTA}║{RESET}  Método: split() tras limpieza • múltiples espacios ignorados • sin puntuación {MAGENTA}║{RESET}
{MAGENTA}╚══════════════════════════════════════════════════════════════════════════════╝{RESET}

{DIM}    Powered by Python + Regex • Contador de palabras nivel dios{RESET}
""")


# ── Programa principal ─────────────────────────────────────────────────────────
print("\n" * 2)
print(f"{CYAN}{'═'*80}{RESET}")
print(f"     {NEGRITA}CONTADOR DE PALABRAS – MODO VISUAL TERMINAL v3.1{RESET}     ")
print(f"     {DIM}Introduce cualquier texto – se limpiarán signos de puntuación{RESET}")
print(f"{CYAN}{'═'*80}{RESET}\n")

try:
    texto = input(f"{CYAN}→ Tu texto → {RESET}")

    # Limpieza y conteo
    texto_limpio = limpiar_texto(texto)
    cantidad = contar_palabras(texto_limpio)

    # Resultado épico
    mostrar_resultado(texto, cantidad)

    # Información adicional (detalle técnico)
    print(f"\n{DIM}Detalles técnicos:{RESET}")
    print(f"   • Palabras encontradas ..: {cantidad}")
    print(f"   • Caracteres originales ..: {len(texto)}")
    print(f"   • Caracteres tras limpieza: {len(texto_limpio)}")
    print(f"   • Método ................: split() + regex limpieza")

except KeyboardInterrupt:
    print(f"\n\n{DIM}Programa terminado por el usuario. ¡Hasta la próxima!{RESET}\n")
    sys.exit(0)