from datetime import datetime
import os

# Colores para la terminal
CYAN = "\033[96m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
ROJO = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
NEGRITA = "\033[1m"
DIM = "\033[2m"

ARCHIVO = "quijote.txt"


def linea_decorativa(ancho=70, simbolo="═"):
    print(f"{MAGENTA}{simbolo * ancho}{RESET}")


def cabecera(titulo):
    linea_decorativa()
    print(f"{CYAN}{NEGRITA}  ★  {titulo.upper()}  ★  {RESET}".center(78))
    print(f"{DIM}{datetime.now().strftime('%Y-%m-%d  %H:%M:%S')}{' ' * 20}archivo: {ARCHIVO}{RESET}")
    linea_decorativa()


def mostrar_contenido_completo():
    try:
        with open(ARCHIVO, "rt", encoding="utf-8") as f:
            contenido = f.read()

        cabecera("CONTENIDO COMPLETO DEL ARCHIVO")
        print(f"{VERDE}{contenido}{RESET}")
        print(f"\n{DIM}Caracteres totales: {len(contenido):,}{RESET}")

    except FileNotFoundError:
        print(f"{ROJO}⚠  El archivo '{ARCHIVO}' no existe{RESET}")
    except Exception as e:
        print(f"{ROJO}Error al leer el archivo: {e}{RESET}")


def mostrar_linea_por_linea():
    try:
        with open(ARCHIVO, "rt", encoding="utf-8") as f:
            lineas = f.readlines()

        cabecera("LECTURA LÍNEA POR LÍNEA (readlines)")
        for i, linea in enumerate(lineas, 1):
            linea_limpia = linea.rstrip("\n")
            print(f"{DIM}{i:3d} │{RESET} {linea_limpia}")
        print(f"\n{DIM}Total líneas: {len(lineas)}{RESET}")

    except Exception as e:
        print(f"{ROJO}Error: {e}{RESET}")


def mostrar_caracteres_por_caracter():
    try:
        with open(ARCHIVO, "rt", encoding="utf-8") as f:
            cabecera("LECTURA DE 8 EN 8 CARACTERES")
            contador = 0
            while True:
                trozo = f.read(8)
                if not trozo:
                    break
                print(f"{AMARILLO}[{contador:04d}]{RESET} → {repr(trozo)}")
                contador += len(trozo)
            print(f"\n{DIM}Total caracteres leídos: {contador:,}{RESET}")

    except Exception as e:
        print(f"{ROJO}Error: {e}{RESET}")


def escribir_ejemplo():
    try:
        with open(ARCHIVO, "wt", encoding="utf-8") as f:
            f.write("En algún lugar de Caracas,\n")
            f.write("de cuyo nombre nadie se acuerda,\n")
            f.write("no ha mucho tiempo que vivía un hidalgo...\n")

        print(f"\n{VERDE}✓  Archivo sobrescrito con éxito{RESET}")

    except Exception as e:
        print(f"{ROJO}Error al escribir: {e}{RESET}")


def agregar_texto():
    try:
        with open(ARCHIVO, "at", encoding="utf-8") as f:
            f.write("\n=== Texto agregado el " + datetime.now().strftime("%Y-%m-%d %H:%M") + " ===\n")
            f.write("¡Qué grande es la vida cuando se vive con pasión!\n")

        print(f"\n{VERDE}✓  Texto agregado al final del archivo{RESET}")

    except Exception as e:
        print(f"{ROJO}Error al agregar texto: {e}{RESET}")


# ────────────────────────────────────────────────
#                PROGRAMA PRINCIPAL
# ────────────────────────────────────────────────

print("\n" * 2)
linea_decorativa(80, "★")
print(f"{MAGENTA}{NEGRITA}           MANEJO DE FICHEROS – NIVEL ÉPICO           {RESET}")
linea_decorativa(80, "★")

print(f"\n{VERDE}Opciones disponibles:{RESET}")
print("  1   Mostrar contenido completo")
print("  2   Mostrar línea por línea (con números)")
print("  3   Mostrar lectura de 8 en 8 caracteres")
print("  4   Sobrescribir archivo (modo 'w')")
print("  5   Agregar texto al final (modo 'a')")
print("  0   Salir\n")

opcion = input(f"{CYAN}Elige una opción → {RESET}")

if opcion == "1":
    mostrar_contenido_completo()
elif opcion == "2":
    mostrar_linea_por_linea()
elif opcion == "3":
    mostrar_caracteres_por_caracter()
elif opcion == "4":
    escribir_ejemplo()
elif opcion == "5":
    agregar_texto()
elif opcion == "0":
    print(f"\n{DIM}¡Hasta la próxima, maestro del I/O!{RESET}\n")
else:
    print(f"{ROJO}Opción no válida{RESET}")

print()
linea_decorativa(80)