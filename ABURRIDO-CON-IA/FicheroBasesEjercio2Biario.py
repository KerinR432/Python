import pickle
import sys
from datetime import datetime

# ── Colores ANSI (funcionan en la mayoría de terminales modernas) ───────────────
CYAN     = "\033[96m"
GREEN    = "\033[92m"
YELLOW   = "\033[93m"
MAGENTA  = "\033[95m"
RED      = "\033[91m"
BLUE     = "\033[94m"
RESET    = "\033[0m"
BOLD     = "\033[1m"
DIM      = "\033[2m"
UNDER    = "\033[4m"

ARCHIVO_BIN = "quijoteBinario.bin"


def linea(ancho=78, char="═"):
    print(f"{MAGENTA}{char * ancho}{RESET}")


def cabecera(titulo):
    linea()
    print(f"{CYAN}{BOLD}  ⚡  {titulo.upper().center(70)}  ⚡  {RESET}")
    print(f"{DIM}{datetime.now().strftime('%Y-%m-%d   %H:%M:%S')}   •   BINARY ARCHIVE v3.1{RESET}")
    linea()


def error(msg):
    print(f"\n{RED}{BOLD}✖  CRITICAL FAILURE{RESET}  →  {msg}\n")
    sys.exit(1)


class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    def __str__(self):
        return f"{self.nombre}"


# ───────────────────────────────────────────────────────────────────────────────
#  1. Escritura individual de objetos
# ───────────────────────────────────────────────────────────────────────────────
print("\n")
cabecera("FASE 1 → SERIALIZACIÓN INDIVIDUAL")

try:
    with open(ARCHIVO_BIN, "wb") as f:
        p1 = Persona("Mohamed")
        p2 = Persona("Feddy")
        pickle.dump(p1, f)
        pickle.dump(p2, f)

    print(f"{GREEN}{BOLD}✓{RESET}  {CYAN}2 entidades{RESET} guardadas con éxito → {ARCHIVO_BIN}")
except Exception as e:
    error(f"No se pudo escribir: {e}")


# ───────────────────────────────────────────────────────────────────────────────
#  2. Lectura individual
# ───────────────────────────────────────────────────────────────────────────────
print("\n")
cabecera("FASE 2 → DESERIALIZACIÓN INDIVIDUAL")

try:
    with open(ARCHIVO_BIN, "rb") as f:
        persona1 = pickle.load(f)
        persona2 = pickle.load(f)

    print(f"{BLUE}┌{'─'*74}┐{RESET}")
    print(f"{BLUE}│{RESET}  Entidad 1     →  {BOLD}{persona1.nombre:^20}{RESET}  {BLUE}│{RESET}")
    print(f"{BLUE}│{RESET}  Entidad 2     →  {BOLD}{persona2.nombre:^20}{RESET}  {BLUE}│{RESET}")
    print(f"{BLUE}└{'─'*74}┘{RESET}")

except Exception as e:
    error(f"No se pudo leer individualmente: {e}")


# ───────────────────────────────────────────────────────────────────────────────
#  3. Escritura y lectura de lista completa (mejor práctica)
# ───────────────────────────────────────────────────────────────────────────────
print("\n")
cabecera("FASE 3 → MODO ÓPTIMO (LISTA COMPLETA)")

try:
    # Preparar datos
    lista_personas = [
        Persona("Mohamed"),
        Persona("Feddy"),
        Persona("Aisha"),
        Persona("Zoe")
    ]

    # Escritura
    with open(ARCHIVO_BIN, "wb") as f:
        pickle.dump(lista_personas, f)

    print(f"{GREEN}{BOLD}✓{RESET}  {len(lista_personas)} entidades empaquetadas en lista")

    # Lectura
    with open(ARCHIVO_BIN, "rb") as f:
        recuperadas = pickle.load(f)

    # ── Visualización estilo Pokédex / Dashboard ───────────────────────────────
    linea(char="─")
    print(f"{YELLOW}   ID   {'NOMBRE':^22}   {'ESTADO':^12}   {YELLOW}")
    linea(char="─")

    for i, p in enumerate(recuperadas, 1):
        print(f"  {CYAN}{i:2d}{RESET}   {BOLD}{p.nombre:<22}{RESET}   {GREEN}ACTIVA{RESET}")

    print(f"\n{DIM}Total recuperados → {len(recuperadas)}{RESET}")
    linea()

except Exception as e:
    error(f"Fallo en modo lista: {e}")


print(f"\n{GREEN}{BOLD}★  Operación completada sin anomalías detectadas  ★{RESET}\n")