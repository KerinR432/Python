"""9. Escribir un programa que nos pida elegir entre cuatro destinos turísticos (Francia,
Italia, Chile o Japón) y dependiendo de nuestra respuesta nos diga cual es la capital de
nuestro destino (París, Roma, Santiago de Chile o Tokio)
"""

num = 0
while num != 5:
    num = int(input("Elige tu destino: \n 1) Francia\n 2) Italia\n 3) Chile\n 4) Japon\n 5) salir\n"))
    match num:
        case 1:
            print("El siguientes destino es paris!!!!")
            num = 5
        case 2:
            print("El siguientes destino es Roma!!!!")
            num = 5
        case 3:
            print("El siguientes destino es Santiago!!!!")
            num = 5
        case 4:
            print("El siguientes destino es Tokio!!!!")
            num = 5
        case 5:
            print("Bien has salido!!!!!")
            num = 5
        case _:
            print("Has introducido mal el numero...")
