"""
6. Escribe un programa usando POO que, tomando el mismo fichero clientes.txt del ejercicio
anterior, tenga una clase que se llame cliente donde guarde la información de los clientes que se
hayan leído del fichero.
José María Morales Vázquez Página 3
Ejercicios genéricos de programación 17
Tu clase debería de tener un constructor para crear el objeto que reciba la línea tal y como se lee del
fichero. Así:
cliente01 = Cliente(“Diego Norrea 28222777J”)
Tu clase deberá de contar con atributos separados para el nombre, el apellido y el NIF.
Debes de crear un método que se llame mostrar que nos muestre la información del cliente por
consola en el siguiente formato:
28222777J – Norrea, Diego
Por último, usando esta clase como soporte, haz un listado del contenido del fichero por consola
que debería de quedar así:
28222777J – Norrea, Diego
07333888X – Perado, Inés
97221345Y - Imedio , Demetrio
22876345M – Rija, Roberto
12987543C – Tosidad, Rubém
32879563V – Adistancia, Armando
18000777H – Tequilla, Germán
"""


class Cliente:
    # El Constructor: Se activa al hacer Cliente("línea del archivo")
    def __init__(self, linea):
        # .split() divide la línea por los espacios en blanco
        datos = linea.split()

        # Guardamos cada trozo en un "atributo" (variable interna)
        self.nombre = datos[0]
        self.apellido = datos[1]
        self.nif = datos[2]

    # El Método: Una función que vive dentro del objeto
    def mostrar(self):
        # Imprime siguiendo el formato: NIF - Apellido, Nombre
        print(f"{self.nif} – {self.apellido}, {self.nombre}")


# --- PARTE PRINCIPAL DEL PROGRAMA ---

# 1. Abrimos el archivo (asegúrate de que clientes.txt esté en la misma carpeta)
try:
    with open("clientes.txt", "r", encoding="utf-8") as archivo:
        # 2. Leemos el archivo línea por línea
        for linea in archivo:
            # Quitamos saltos de línea invisibles con .strip()
            linea_limpia = linea.strip()

            # Si la línea no está vacía, creamos el objeto y lo mostramos
            if linea_limpia:
                nuevo_cliente = Cliente(linea_limpia)
                nuevo_cliente.mostrar()

except FileNotFoundError:
    print("Error: No se encontró el archivo 'clientes.txt'")