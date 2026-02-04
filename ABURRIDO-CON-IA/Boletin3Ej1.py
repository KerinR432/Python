import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.layout import Layout
from rich.live import Live

console = Console()


def halo_terminal_header():
    header_text = "[bold cyan]UNSC - DATA ACCESS TERMINAL v3.117[/bold cyan]\n[dim]LOCATING ARCHIVE... [SUCCESS][/dim]"
    console.print(Panel(header_text, border_style="bright_blue", expand=False))


def access_granted_sequence():
    with Progress(
            SpinnerColumn(),
            TextColumn("[bold green]{task.description}"),
            transient=True,
    ) as progress:
        task = progress.add_task(description="DECRYPTING DATA CORE...", total=None)
        time.sleep(1.5)

    console.print("\n[bold green]>>> ACCESS GRANTED. WELCOME BACK, RECLAIMER.[/bold green]\n")


def halo_auth_system():
    halo_terminal_header()

    # Primera entrada
    password_save = Prompt.ask("[bold white]SET NEW ACCESS KEY[/bold white]", password=True)

    match = False
    while not match:
        confirm_password = Prompt.ask("[bold yellow]CONFIRM SECURITY OVERRIDE[/bold yellow]", password=True)

        if confirm_password == password_save:
            match = True
            access_granted_sequence()
        else:
            console.print("[bold red]!! ERROR: FRAGMENTED KEY DATA. RETRY AUTHENTICATION !![/bold red]")
            console.print("[dim]------------------------------------------------[/dim]")


if __name__ == "__main__":
    halo_auth_system()