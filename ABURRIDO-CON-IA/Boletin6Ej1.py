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

# ── Mensajes con formato visual ────────────────────────────────────────────────
def marco(titulo, color=CYAN, ancho=70):
    linea = f"{color}═{RESET}" * ancho
    print(f"{color}╔{linea}╗{RESET}")
    print(f"{color}║{RESET}  {NEGRITA}{titulo.center(ancho-4)}{RESET}  {color}║{RESET}")
    print(f"{color}╚{linea}╝{RESET}\n")


def exito(cp):
    ahora = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    print(f"""
{MAGENTA}╔{'═'*68}╗{RESET}
{MAGENTA}║{RESET}  {'¡CÓDIGO POSTAL VÁLIDO!':^66}  {MAGENTA}║{RESET}
{MAGENTA}╠{'═'*68}╣{RESET}
{MAGENTA}║{RESET}  Código: {VERDE}{NEGRITA}{cp:^60}{RESET}  {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Zona:   {CYAN}Madrid capital y alrededores{RESET:<47}  {MAGENTA}║{RESET}
{MAGENTA}║{RESET}  Validado: {DIM}{ahora}{RESET:<54}  {MAGENTA}║{RESET}
{MAGENTA}╠{'─'*68}╣{RESET}
{MAGENTA}║{RESET}  {VERDE}✓ Tu paquete ya está en camino hacia la Comunidad de Madrid ✓{RESET}  {MAGENTA}║{RESET}
{MAGENTA}╚{'═'*68}╝{RESET}

    {VERDE}¡Gracias por confiar en nosotros! 🚚📦{RESET}
""")


def fallo(cp):
    print(f"""
{ROJO}╔{'═'*68}╗{RESET}
{ROJO}║{RESET}  {'CÓDIGO POSTAL NO VÁLIDO':^66}  {ROJO}║{RESET}
{ROJO}╠{'═'*68}╣{RESET}
{ROJO}║{RESET}  Introducido: {AMARILLO}{cp:^52}{RESET}  {ROJO}║{RESET}
{ROJO}║{RESET}  Formato esperado: {CYAN}28XXX{RESET}  (5 dígitos, empieza por 28)  {ROJO}║{RESET}
{ROJO}╠{'─'*68}╣{RESET}
{ROJO}║{RESET}  {DIM}Ejemplos válidos:{RESET}  28001   28080   28039   28100   28232  {ROJO}║{RESET}
{ROJO}║{RESET}                                                                  {ROJO}║{RESET}
{ROJO}╚{'═'*68}╝{RESET}

    {ROJO}Por favor, inténtalo de nuevo 😔{RESET}
""")


def cabecera():
    print("\n" * 2)
    print(f"{CYAN}{'★' * 25}{RESET}   VALIDACIÓN CÓDIGO POSTAL MADRID   {CYAN}{'★' * 25}{RESET}")
    print(f"  {DIM}Solo códigos que empiecen por 28 (Comunidad de Madrid){RESET}")
    print(f"{CYAN}{'═' * 78}{RESET}\n")


# ── Expresión regular corregida y más clara ────────────────────────────────────
# 28 seguido exactamente de 3 dígitos (total 5 caracteres)
PATRON_MADRID = r"^28\d{3}$"


def es_codigo_postal_madrid(codigo: str) -> bool:
    return bool(re.match(PATRON_MADRID, codigo.strip()))


# ── Programa principal ─────────────────────────────────────────────────────────
def main():
    cabecera()

    while True:
        try:
            entrada = input(f"{CYAN}Introduce código postal (28XXX): {RESET}").strip()

            if not entrada:
                print(f"{AMARILLO}→ No has escrito nada. Inténtalo de nuevo.{RESET}\n")
                continue

            if es_codigo_postal_madrid(entrada):
                exito(entrada)
                break
            else:
                fallo(entrada)

        except KeyboardInterrupt:
            print(f"\n\n{DIM}Programa terminado por el usuario. ¡Hasta pronto!{RESET}\n")
            break
        except Exception as e:
            print(f"{ROJO}Error inesperado: {e}{RESET}\n")


if __name__ == "__main__":
    main()