import random

# ── Colores ANSI épicos (Pokédex retro-futurista) ──────────────────────────────
NEGRO = "\033[30m"
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CIAN = "\033[96m"
BLANCO = "\033[97m"
GRIS = "\033[90m"
RESET = "\033[0m"
NEGRITA = "\033[1m"
DIM = "\033[2m"
SUBRAYADO = "\033[4m"
INVERTIDO = "\033[7m"

# Colores por tipo Pokémon (espectaculares)
COLORES_TIPO = {
    "normal": GRIS,
    "agua": CIAN,
    "fuego": ROJO,
    "planta": VERDE,
    "volador": AZUL,
    "lucha": AMARILLO,
    "veneno": MAGENTA,
    "eléctrico": AMARILLO,
    "tierra": NEGRO + "\033[43m",  # Fondo amarillo para tierra
    "roca": GRIS,
    "psíquico": MAGENTA,
    "hielo": CIAN + "\033[47m",  # Fondo blanco
    "bicho": VERDE,
    "fantasma": MAGENTA + "\033[40m",  # Fondo negro
    "dragón": NEGRITA + CIAN
}

TIPOS_VALIDOS = {
    "Normal", "Agua", "Fuego", "Planta", "Volador", "Lucha", "Veneno",
    "Eléctrico", "Tierra", "Roca", "Psíquico", "Hielo", "Bicho", "Fantasma", "Dragón"
}

EMOJIS_TIPO = {
    "Normal": "⭐", "Agua": "💧", "Fuego": "🔥", "Planta": "🌿",
    "Volador": "🕊️", "Lucha": "🥊", "Veneno": "☠️", "Eléctrico": "⚡",
    "Tierra": "⛰️", "Roca": "🪨", "Psíquico": "🧠", "Hielo": "❄️",
    "Bicho": "🐛", "Fantasma": "👻", "Dragón": "🐉"
}


class Pokemon:
    def __init__(self, codigo, nombre, tipos, evolucion=None):
        if not (1 <= codigo <= 151):
            raise ValueError("Código debe estar entre 1 y 151")

        if not isinstance(tipos, (list, tuple)) or len(tipos) not in (1, 2):
            raise ValueError("Tipos debe ser lista/tupla de 1-2 tipos válidos")

        for t in tipos:
            t_lower = t.lower()
            if t_lower not in [tv.lower() for tv in TIPOS_VALIDOS]:
                raise ValueError(f"Tipo inválido: {t}")

        self.__codigo = codigo
        self.__nombre = nombre.title()
        self.__tipos = [t.title() for t in tipos]
        self._evolucion = evolucion
        self.__pv_max = 100
        self.__pv = random.randint(50, self.__pv_max)

    # ── Getters (sin setters) ───────────────────────────────────────────────────
    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def tipos(self):
        return self.__tipos

    @property
    def pv(self):
        return self.__pv

    @property
    def pv_max(self):
        return self.__pv_max

    @property
    def proximo_evolucion(self):
        return self._evolucion.nombre if self._evolucion else "Ninguna"

    # ── Evolución ───────────────────────────────────────────────────────────────
    def evoluciona(self):
        if self._evolucion is None:
            print(f"{AMARILLO}¡{self.nombre} no tiene más evoluciones! 🌟{RESET}")
            return self
        return self._evolucion

    # ── Combate (lógica corregida: turno completo ataque-defensa) ────────────────
    def puede_combatir(self, oponente):
        return self.pv > 0 and oponente.pv > 0

    def combate_pokemon(self, oponente):
        if not self.puede_combatir(oponente):
            print(f"{ROJO}¡No se puede combatir! Uno o ambos Pokémon están debilitados! ⚠️{RESET}")
            return

        # Ataque del jugador
        dano = random.randint(25, 75)
        oponente.__pv = max(0, oponente.__pv - dano)
        print(f"{CIAN}¡{self.nombre} ataca! Dañó {dano} PV a {oponente.nombre}! ⚔️{RESET}")

        if oponente.pv <= 0:
            print(f"{ROJO}¡{oponente.nombre} ha sido NOQUEADO! 😵💥{RESET}")
            return

        # Contraataque del oponente
        dano_op = random.randint(25, 75)
        self.__pv = max(0, self.__pv - dano_op)
        print(f"{MAGENTA}¡{oponente.nombre} contraataca! Dañó {dano_op} PV a {self.nombre}! 🔄{RESET}")

        if self.pv <= 0:
            print(f"{ROJO}¡{self.nombre} ha sido DERROTADO! 💔{RESET}")

    # ── MOSTRAR POKÉMON – F-STRING ÉPICO 🌌 ─────────────────────────────────────
    def mostrar_pokemon(self):
        color_principal = COLORES_TIPO.get(self.tipos[0].lower(), GRIS)
        emoji_principal = EMOJIS_TIPO.get(self.tipos[0], "⭐")

        # Barra de PV ultra visual
        pv_ratio = self.pv / self.pv_max
        barra_pv_len = 30
        llenado = int(pv_ratio * barra_pv_len)
        barra_pv = (
                f"{VERDE}█{RESET}" * llenado +
                f"{ROJO}█{RESET}" * (barra_pv_len - llenado)
        )

        tipos_str = " / ".join(self.tipos)
        tipos_emojis = " ".join(EMOJIS_TIPO.get(t, "⭐") for t in self.tipos)

        informe = f"""
{color_principal}{NEGRITA}
╔══════════════════════════════════════════════════════════════════════════════╗{RESET}
║{color_principal}  {emoji_principal:^3}  {NEGRITA}{self.nombre.upper():^58}  {emoji_principal}  {color_principal}║{RESET}
╠{color_principal}{'═' * 73}╣{RESET}
║{RESET}  {CIAN}#{self.codigo:>3}{RESET} │ {AMARILLO}{tipos_str:<20}{RESET} │ {DIM}Evolución: {self.proximo_evolucion:<20}{RESET}  ║
║{RESET}  {GRIS}Tipos:{RESET} {tipos_emojis:<25} │ {NEGRITA}PV:{RESET} [{barra_pv}] {self.pv}/{self.pv_max}  ║
╠{color_principal}{'─' * 73}╣{RESET}
║{RESET}                                                                 {color_principal}║{RESET}
║{RESET}  {DIM}¡Entrena duro y llegarás a la cima de la Liga Pokémon!{RESET:^65}  {color_principal}║{RESET}
║{RESET}                                                                   {color_principal}║{RESET}
╚{color_principal}{'═' * 73}╝{RESET}{NEGRITA}
{color_principal}    ¡{self.nombre} está listo para la batalla! 🔥⚡🌿    {RESET}
        """
        print(informe)


# ── DEMO ÉPICA ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"{MAGENTA}{'═' * 90}{RESET}")
    print(f"{CIAN}{NEGRITA}          POKÉDEX GEN 1 – EVOLUCIONES & COMBATE ULTRA v2.0          {RESET}")
    print(f"{MAGENTA}{'═' * 90}{RESET}\n")

    # Cadena de evolución Bulbasaur → Ivysaur → Venusaur
    p3 = Pokemon(3, "Venusaur", ["Planta", "Veneno"])
    p2 = Pokemon(2, "Ivysaur", ["Planta", "Veneno"], p3)
    p1 = Pokemon(1, "Bulbasaur", ["Planta", "Veneno"], p2)

    print("📋 ESTADO INICIAL:")
    p1.mostrar_pokemon()
    p2.mostrar_pokemon()
    p3.mostrar_pokemon()

    print("\n🔄 EVOLUCIONES:")
    p1 = p1.evoluciona()  # → Ivysaur
    p3 = p3.evoluciona()  # No evoluciona

    print("\n📋 DESPUÉS DE EVOLUCIONES:")
    p1.mostrar_pokemon()
    p3.mostrar_pokemon()

    print("\n⚔️  BATALLA ÉPICA: IVYSAUR vs VENUSAUR")
    p1.combate_pokemon(p3)
    print("\n📊 ESTADO POST-BATALLA 1:")
    p1.mostrar_pokemon()
    p3.mostrar_pokemon()

    print("\n🔥 SEGUNDO ASALTO:")
    p1.combate_pokemon(p3)