import re
from datetime import datetime

# ── Colores ANSI (funcionan en la mayoría de terminales modernas) ───────────────
CYAN     = "\033[96m"
VERDE    = "\033[92m"
AMARILLO = "\033[93m"
ROJO     = "\033[91m"
MAGENTA  = "\033[95m"
RESET    = "\033[0m"
NEGRITA  = "\033[1m"
DIM      = "\033[2m"
BLANCO   = "\033[97m"

# ── Mensajes con formato visual atractivo ──────────────────────────────────────
def marco_exito(numero):
    ahora = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    print(f"""
{VERDE}╔{'═'*72}╗{RESET}
{VERDE}║{RESET}  {'¡NÚMERO DE TELÉFONO VÁLIDO!':^70}  {VERDE}║{RESET}
{VERDE}╠{'═'*72}╣{RESET}
{VERDE}║{RESET}  Número: {NEGRITA}{CYAN}{numero:^60}{RESET}  {VERDE}║{RESET}
{VERDE}║{RESET}  Tipo:   {AMARILLO}{'Móvil español (6/7/8/9)' if numero[0] in '6789' else 'Fijo / Móvil'}{RESET:<54}  {VERDE}║{RESET}
{VERDE}║{RESET}  Validado: {DIM}{ahora}{RESET:<58}  {VERDE}║{RESET}
{VERDE}╠{'─'*72}╣{RESET}
{VERDE}║{RESET}  {VERDE}✓ Formato correcto: 9 dígitos comenzando por 6,7,8 o 9 ✓{RESET}  {VERDE}║{RESET}
{VERDE}╚{'═'*72}╝{RESET}

    {VERDE}¡Gracias por tu consulta! 📱✨{RESET}
""")


def marco_error(numero, motivo=""):
    print(f"""
{ROJO}╔{'═'*72}╗{RESET}
{ROJO}║{RESET}  {'NÚMERO NO VÁLIDO':^70}  {ROJO}║{RESET}
{ROJO}╠{'═'*72}╣{RESET}
{ROJO}║{RESET}  Introducido: {AMARILLO}{numero or '(vacío)':^52}{RESET}  {ROJO}║{RESET}
{ROJO}║{RESET}  Motivo:     {DIM}{motivo or 'No cumple el formato esperado'}{RESET:<54}  {ROJO}║{RESET}
{ROJO}╠{'─'*72}╣{RESET}
{ROJO}║{RESET}  Formato esperado:{RESET} {CYAN}6xxxxxxxx  7xxxxxxxx  8xxxxxxxx  9xxxxxxxx{RESET}  {ROJO}║{RESET}
{ROJO}║{RESET}  (exactamente 9 dígitos, sin espacios ni prefijos internacionales)   {ROJO}║{RESET}
{ROJO}╚{'═'*72}╝{RESET}

    {ROJO}Por favor, inténtalo de nuevo 😔{RESET}
""")


def cabecera():
    print("\n" * 2)
    print(f"{CYAN}{'═'*80}{RESET}")
    print(f"  {NEGRITA}{CYAN}VALIDADOR DE NÚMEROS DE TELÉFONO ESPAÑOLES (9 dígitos){RESET}  ")
    print(f"  {DIM}Empieza por 6, 7, 8 o 9 – sin espacios ni prefijos (+34){RESET}")
    print(f"{CYAN}{'═'*80}{RESET}\n")


# ── Patrón más realista y estricto ─────────────────────────────────────────────
# Empieza por 6,7,8,9 y exactamente 8 dígitos más → total 9
PATRON_TELEFONO = r"^[6-9]\d{8}$"


def es_numero_telefono_valido(texto: str) -> bool:
    return bool(re.match(PATRON_TELEFONO, texto.strip()))


# ── Programa principal ─────────────────────────────────────────────────────────
def main():
    cabecera()

    while True:
        entrada = input(f"{CYAN}Introduce número de teléfono (9 dígitos): {RESET}").strip()

        if not entrada:
            marco_error("", "No has introducido ningún número")
            continue

        # Quitamos posibles espacios y guiones que la gente suele poner
        numero_limpio = re.sub(r'[\s\-\(\)\+]', '', entrada)

        # Intentamos convertir a entero para validar que son solo dígitos
        try:
            int(numero_limpio)
        except ValueError:
            marco_error(entrada, "Contiene caracteres que no son dígitos")
            continue

        if len(numero_limpio) != 9:
            marco_error(numero_limpio, f"Longitud incorrecta ({len(numero_limpio)} dígitos en lugar de 9)")
            continue

        if es_numero_telefono_valido(numero_limpio):
            marco_exito(numero_limpio)
            break
        else:
            marco_error(numero_limpio)


if __name__ == "__main__":321498491
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{DIM}Programa terminado por el usuario. ¡Hasta la próxima!{RESET}\n")