"""Programa que pide una contraseña dos veces y repite el proceso hasta que ambas coincidan."""

correcto = False

# Pedimos la contraseña inicial
contraseña_guardada = input("🔒 Introduce una contraseña: ").strip()

# Repetimos hasta que coincida
while not correcto:
    intento = input("🔁 Repite la contraseña para confirmar: ").strip()
    if intento == contraseña_guardada:
        print("✅ Contraseña confirmada correctamente. ¡Bienvenido! 🎉")
        correcto = True
    else:
        print("❌ Las contraseñas no coinciden. Intenta de nuevo.\n")
