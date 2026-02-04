import time
import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.live import Live

console = Console()


def typewriter_effect(text, style="bold white", delay=0.03):
    """Simula la escritura de una terminal antigua."""
    for char in text:
        console.print(char, style=style, end="")
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Salto de línea al terminar


def halo_header():
    header = """
    [bright_blue]====================================================
    TERMINAL 01 - LOCALIZACIÓN: ARCA (INSTALACIÓN 00)
    SISTEMA OPERATIVO: MONITOR 343 GUILTY SPARK
    ====================================================[/bright_blue]
    """
    console.print(header)


def auth_system():
    halo_header()

    # Primera entrada (oculta para mayor realismo)
    typewriter_effect(">>> ESTABLECIENDO PROTOCOLO DE SEGURIDAD...", "dim cyan")
    pass_save = Prompt.ask("[bold white]INTRODUCE CLAVE DE ACCESO RECLAMADOR[/bold white]", password=True)

    intentos_fallidos = 0
    match = False

    while not match:
        typewriter_effect("\n>>> PENDIENTE DE CONFIRMACIÓN...", "cyan")
        confirm_pass = Prompt.ask("[bold yellow]RE-INTRODUCE CLAVE PARA VERIFICACIÓN[/bold yellow]", password=True)

        if confirm_pass == pass_save:
            match = True
            # Secuencia final de éxito
            typewriter_effect("\n[bold green]AUTENTICACIÓN COMPLETADA.[/bold green]", delay=0.05)
            typewriter_effect(
                f"[bold white]RECLAMADOR RECONOCIDO TRAS {intentos_fallidos} INTENTO(S) FALLIDO(S).[/bold white]",
                delay=0.05)

            console.print(Panel(
                "[bold bright_white]ACCESO TOTAL CONCEDIDO[/bold bright_white]\n[dim]Iniciando descarga de datos del Índice...[/dim]",
                title="[green]ESTADO: ONLINE[/green]",
                border_style="green",
                padding=(1, 2)
            ))
        else:
            intentos_fallidos += 1
            console.print("[bold red]!! ERROR DE SINCRONIZACIÓN !![/bold red]")
            typewriter_effect(f"ADVERTENCIA: Intento de intrusión detectado (#{intentos_fallidos}).", "red", 0.02)
            console.print("[dim]------------------------------------------------[/dim]")


if __name__ == "__main__":
    try:
        auth_system()
    except KeyboardInterrupt:
        console.print("\n[red]SISTEMA ABORTADO POR EL USUARIO.[/red]")