from datetime import datetime
import sys

# ── Colores ANSI (funcionan en la mayoría de terminales modernas) ───────────────
CYAN     = "\033[96m"
VERDE    = "\033[92m"
AMARILLO = "\033[93m"
BLANCO   = "\033[97m"
ROJO     = "\033[91m"
MAGENTA  = "\033[95m"
RESET    = "\033[0m"
NEGRITA  = "\033[1m"
DIM      = "\033[2m"
SUBRAYADO = "\033[4m"


COLORES_VALIDOS = {"amarillo", "verde", "blanco", "cyan"}


class Nota:
    def __init__(self, titulo="", descripcion="", color="amarillo", fecha=None):
        if fecha is None:
            fecha = datetime.now().strftime("%Y-%m-%d  %H:%M")

        self.titulo = titulo.strip()
        self.descripcion = descripcion.strip()
        self.color = color.lower() if color.lower() in COLORES_VALIDOS else "amarillo"
        self.fecha_creacion = fecha

        # Para simular que la nota está "activa"
        self._eliminada = False

    @property
    def color_ansi(self):
        match self.color:
            case "amarillo": return AMARILLO
            case "verde":    return VERDE
            case "blanco":   return BLANCO
            case "cyan":     return CYAN
            case _:          return RESET

    def crear(self, titulo, descripcion, color="amarillo"):
        """Método para (re)crear / actualizar la nota"""
        if self._eliminada:
            print(f"{ROJO}Esta nota fue eliminada. No se puede modificar.{RESET}")
            return

        self.titulo = titulo.strip()
        self.descripcion = descripcion.strip()
        self.color = color.lower() if color.lower() in COLORES_VALIDOS else "amarillo"
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d  %H:%M")
        self._eliminada = False
        print(f"{VERDE}✓ Nota actualizada / creada{RESET}")

    def eliminar(self):
        """Marca la nota como eliminada (soft delete)"""
        self._eliminada = True
        print(f"{ROJO}🗑  Nota eliminada{RESET}")

    def restaurar(self):
        """Restaura una nota eliminada (opcional)"""
        self._eliminada = False
        print(f"{VERDE}↺  Nota restaurada{RESET}")

    def mostrar(self):
        """Muestra la nota con formato visual atractivo"""
        if self._eliminada:
            print(f"""
{MAGENTA}┌{'─'*68}┐{RESET}
{MAGENTA}│{RESET}  {'NOTA ELIMINADA':^66}  {MAGENTA}│{RESET}
{MAGENTA}└{'─'*68}┘{RESET}
            """)
            return

        color = self.color_ansi
        marco = f"{color}═{RESET}"

        print(f"""
{color}╔{'═'*70}╗{RESET}
{color}║{RESET}  {NEGRITA}{self.titulo.upper():^68}{RESET}  {color}║{RESET}
{color}╠{'═'*70}╣{RESET}
{color}║{RESET}  {DIM}{self.fecha_creacion:^68}{RESET}  {color}║{RESET}
{color}╠{'─'*70}╣{RESET}
{color}║{RESET}
{color}║{RESET}    {self.descripcion or '(sin descripción)'}
{color}║{RESET}
{color}╚{'═'*70}╝{RESET}

    {DIM}Color:{RESET} {self.color.capitalize():<10}   {DIM}Estado:{RESET} {'Activa' if not self._eliminada else 'Eliminada'}
""")

    def __str__(self):
        return f"Nota(título={self.titulo!r}, color={self.color}, fecha={self.fecha_creacion})"


# ───────────────────────────────────────────────────────────────────────────────
#                             PRUEBAS
# ───────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":

    print("\n" + "="*80)
    print("           GESTOR DE NOTAS – MODO VISUAL TERMINAL v1.7          ")
    print("="*80 + "\n")

    # Nota 1
    n1 = Nota(
        titulo="Comprar ingredientes para la cena",
        descripcion="Queso curado, tomate cherry, albahaca fresca, jamón serrano y una botella de Rioja reserva.",
        color="verde"
    )
    n1.mostrar()

    # Nota 2
    n2 = Nota()
    n2.crear(
        "Recordatorio importante",
        "Llamar al banco antes del viernes para confirmar la transferencia internacional.",
        color="cyan"
    )
    n2.mostrar()

    # Nota 3 – eliminada
    n3 = Nota("Idea de proyecto 2026", "Aplicación de hábitos con gamificación y streaks visuales", "amarillo")
    n3.mostrar()

    print("\n" + "-"*80)
    print("   → Eliminamos la nota 3")
    print("-"*80 + "\n")
    n3.eliminar()
    n3.mostrar()

    # Restaurar (opcional, solo para demostrar)
    # n3.restaurar()
    # n3.mostrar()