import time
import sys
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich.style import Style

console = Console()


def typewriter_effect(text, style="bold #E5B567"):
    """Simula la carga de datos de las terminales de Halo."""
    for char in text:
        console.print(char, style=style, end="")
        sys.stdout.flush()
        time.sleep(0.03)
    print()


def halo_terminal():
    # Limpiar pantalla (opcional)
    console.clear()

    # --- ENCABEZADO ESTILO HALO 3 ---
    header_text = Text("FRAGMENTO DE DATOS: 04-34-299 // REGISTRO DE IDENTIDAD", style="italic #00D7FF")
    console.print(Panel(header_text, border_style="#E5B567", subtitle="[ESTADO: CONECTADO]"))

    print("\n")

    # --- PROCESO DE ENTRADA ---
    # Usamos colores ámbar clásicos de los terminales ocultos
    typewriter_effect("> INICIANDO SECUENCIA DE IDENTIFICACIÓN...")
    time.sleep(0.5)

    nombre = console.input("[bold #00D7FF]>> INTRODUCE NOMBRE DE SUJETO:[/] ").strip()
    apellidos = console.input("[bold #00D7FF]>> INTRODUCE APELLIDOS DE SUJETO:[/] ").strip()

    print("\n")
    typewriter_effect("> PROCESANDO EN CADENA DE DATOS...", style="#00D7FF")

    # Simulación de carga estética
    with console.status("[bold #E5B567]Indexando...", spinner="bouncingBar"):
        time.sleep(1.5)

    # --- RESULTADO FINAL (FORMATO SOLICITADO) ---
    # Formateamos como: Apellidos, Nombre
    resultado_formateado = f"{apellidos.title()}, {nombre.title()}"

    content = Text()
    content.append("\nACCESO CONCEDIDO\n", style="bold green")
    content.append("-" * 30 + "\n", style="#E5B567")
    content.append(f"USUARIO: {resultado_formateado}\n", style="bold white")
    content.append("-" * 30 + "\n", style="#E5B567")
    content.append("\n'Siete niveles de acceso. Un solo guardián.'", style="italic grey50")

    # Panel principal que emula la estética de la imagen que enviaste
    panel_final = Panel(
        content,
        title="[bold #E5B567]TERMINAL 01[/]",
        border_style="#E5B567",
        padding=(1, 2),
        width=60
    )

    console.print(panel_final)


if __name__ == "__main__":
    try:
        halo_terminal()
    except KeyboardInterrupt:
        console.print("\n[red]CONEXIÓN INTERRUMPIDA POR EL RECLAMADOR.[/]")