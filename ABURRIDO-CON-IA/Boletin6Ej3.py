import re
from datetime import datetime

# ── Colores ANSI (compatibles con la mayoría de terminales modernas) ───────────
CYAN     = "\033[96m"
VERDE    = "\033[92m"
AMARILLO = "\033[93m"
ROJO     = "\033[91m"
MAGENTA  = "\033[95m"
RESET    = "\033[0m"
NEGRITA  = "\033[1m"
DIM      = "\033[2m"
BLANCO   = "\033[97m"

# ── Plantillas visuales ────────────────────────────────────────────────────────
def marco_exito(numero):
    ahora = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    print(f"""
{VERDE}╔{'═'*78}╗{RESET}
{VERDE}║{RESET}  {'¡NÚMERO ESPAÑOL VÁLIDO DETECTADO!':^76}  {VERDE}║{RESET}
{VERDE}╠{'═'*78}╣{RESET}
{VERDE}║{RESET}  Número completo: {CYAN}{NEGRITA}{numero:^58}{RESET}  {VERDE}║{RESET}
{VERDE}║{RESET}  Prefijo:          {AMARILLO}+34{RESET}  (España)                                 {VERDE}║{RESET}
{VERDE}║{RESET}  Validado el:      {DIM}{ahora}{RESET}                                 {VERDE}║{RESET}
{VERDE}╠{'─'*78}╣{RESET}
{VERDE}║{RESET}          {VERDE}✓ Formato internacional correcto ✓{RESET}                           {VERDE}║{RESET}
{VERDE}║{RESET}     Llamada autorizada → Conectando con destino España... 📲✨          {VERDE}║{RESET}
{VERDE}╚{'═'*78}╝{RESET}

          {VERDE}¡Listo para la comunicación! 🌍🇪🇸{RESET}
""")


def marco_error(numero, motivo=""):
    print(f"""
{ROJO}╔{'═'*78}╗{RESET}
{ROJO}║{RESET}  {'FORMATO NO VÁLIDO':^76}  {ROJO}║{RESET}
{ROJO}╠{'═'*78}╣{RESET}
{ROJO}║{RESET}  Introducido: {AMARILLO}{numero or '(vacío)':^60}{RESET}  {ROJO}║{RESET}
{ROJO}║{RESET}  Problema:    {DIM}{motivo or 'No coincide con +34 + espacio + 9 dígitos'}{RESET:<60}  {ROJO}║{RESET}
{ROJO}╠{'─'*78}╣{RESET}
{ROJO}║{RESET}  Formato esperado exactamente:{RESET}                                      {ROJO}║{RESET}
{ROJO}║{RESET}     {CYAN}+34 912233444{RESET}   o   {CYAN}+34 655123456{RESET}                                 {ROJO}║{RESET}
{ROJO}║{RESET}     (prefijo +34, un espacio, exactamente 9 dígitos)                     {ROJO}║{RESET}
{ROJO}╚{'═'*78}╝{RESET}

          {ROJO}Vuelve a intentarlo por favor... 📴{RESET}
""")


def cabecera():
    print("\n" * 2)
    print(f"{CYAN}{'═'*90}{RESET}")
    print(f"   {NEGRITA}VALIDADOR INTERNACIONAL DE TELÉFONOS ESPAÑOLES (+34) v2.1{RESET}   ")
    print(f"   {DIM}Formato estricto: +34[espacio]XXXXXXXXX{RESET}")
    print(f"{CYAN}{'═'*90}{RESET}\n")


# ── Patrón mejorado (más estricto y realista) ──────────────────────────────────
# Obliga a: +34 + UN espacio + exactamente 9 dígitos
PATRON_TELEFONO_ES = r'^\+34 \d{9}$'


def es_telefono_espana_valido(texto: str) -> bool:
    return bool(re.match(PATRON_TELEFONO_ES, texto.strip()))


# ── Programa principal ─────────────────────────────────────────────────────────
def main():
    cabecera()

    while True:
        entrada = input(f"{CYAN}Introduce número con prefijo internacional → {RESET}").strip()

        if not entrada:
            marco_error("", "No has escrito nada")
            continue

        # Normalizamos espacios múltiples → uno solo
        entrada_normalizada = re.sub(r'\s+', ' ', entrada.strip())

        if es_telefono_espana_valido(entrada_normalizada):
            marco_exito(entrada_normalizada)
            break
        else:
            # Diagnóstico rápido del error
            motivo = ""
            if not entrada_normalizada.startswith("+34"):
                motivo = "Debe empezar exactamente por +34"
            elif " " not in entrada_normalizada[3:]:
                motivo = "Falta el espacio después de +34"
            elif len(re.sub(r'[^0-9]', '', entrada_normalizada)) != 11:
                motivo = "Deben ser exactamente 9 dígitos después del prefijo"
            else:
                motivo = "Formato incorrecto"

            marco_error(entrada, motivo)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{DIM}Programa terminado por el usuario. ¡Hasta luego!{RESET}\n")