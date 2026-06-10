# APUNTE DE EXAMEN PYTHON (RESUMEN RAPIDO)

## Como usar este apunte en examen
- Usa `Ctrl+F` y busca por palabra clave: `if`, `for`, `list`, `dict`, `try`, `class`, etc.
- Copia y adapta los bloques de codigo.
- Si dudas de sintaxis: revisa primero seccion 1, 2 y 3.

---

## 0) Plantilla base para casi cualquier ejercicio

```python
# 1. Entrada
# 2. Proceso
# 3. Salida

def main():
    # Entrada
    dato = input("Introduce un dato: ")

    # Proceso
    resultado = dato.strip().upper()

    # Salida
    print("Resultado:", resultado)


if __name__ == "__main__":
    main()
```

---

## 1) Variables y tipos

```python
nombre = "Ana"          # str
edad = 19               # int
altura = 1.68           # float
aprobado = True         # bool
nada = None             # NoneType
```

### Conversiones tipicas

```python
x = int("25")
y = float("3.14")
z = str(100)
b = bool(1)             # True
```

### Ver tipo

```python
print(type(x))
```

---

## 2) Entrada y salida

```python
nombre = input("Nombre: ")
edad = int(input("Edad: "))
print("Hola", nombre)
print(f"{nombre} tiene {edad} anos")
```

### f-strings utiles

```python
precio = 12.5
print(f"Precio: {precio:.2f} EUR")
```

---

## 3) Operadores

### Aritmeticos

```python
+  -  *  /  //  %  **
```

### Comparacion

```python
==  !=  >  <  >=  <=
```

### Logicos

```python
and  or  not
```

### Asignacion compacta

```python
x += 1
x -= 2
x *= 3
```

---

## 4) Condicionales (`if`, `elif`, `else`)

```python
nota = float(input("Nota: "))

if nota >= 9:
    print("Sobresaliente")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

### Condicional en una linea

```python
mensaje = "Mayor" if edad >= 18 else "Menor"
```

---

## 5) Bucles

### `for`

```python
for i in range(5):
    print(i)  # 0,1,2,3,4
```

```python
for i in range(2, 10, 2):
    print(i)  # 2,4,6,8
```

### `while`

```python
n = 3
while n > 0:
    print(n)
    n -= 1
```

### `break`, `continue`, `pass`

```python
for n in range(10):
    if n == 3:
        continue
    if n == 8:
        break
    print(n)
```

---

## 6) Cadenas (`str`)

```python
texto = "  Python es util  "
print(texto.lower())
print(texto.upper())
print(texto.strip())
print(texto.replace("util", "genial"))
print(texto.count("o"))
print(texto.startswith("  Py"))
```

### Slicing

```python
s = "python"
print(s[0])      # p
print(s[-1])     # n
print(s[1:4])    # yth
print(s[::-1])   # nohtyp
```

### Comprobar contenido

```python
"py" in "python"           # True
"123".isdigit()            # True
"hola".isalpha()           # True
"hola123".isalnum()        # True
```

---

## 7) Listas

```python
nums = [4, 1, 7]
nums.append(9)
nums.insert(1, 99)
nums.remove(7)
ultimo = nums.pop()
nums.sort()
nums.reverse()
print(len(nums))
```

### Recorrer lista

```python
for n in nums:
    print(n)

for i, n in enumerate(nums):
    print(i, n)
```

### Comprension de listas

```python
cuadrados = [x * x for x in range(6)]
pares = [x for x in range(10) if x % 2 == 0]
```

---

## 8) Tuplas y conjuntos

### Tupla (inmutable)

```python
punto = (3, 5)
x, y = punto
```

### Set (sin repetidos)

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # union
print(a & b)   # interseccion
print(a - b)   # diferencia
```

---

## 9) Diccionarios

```python
persona = {
    "nombre": "Ana",
    "edad": 20
}

print(persona["nombre"])
print(persona.get("dni", "No existe"))
persona["edad"] = 21
persona["ciudad"] = "Vigo"
```

### Recorrido

```python
for clave in persona:
    print(clave, persona[clave])

for clave, valor in persona.items():
    print(clave, valor)
```

---

## 10) Funciones

```python
def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("Luis"))
```

### Parametros por defecto

```python
def potencia(base, exp=2):
    return base ** exp
```

### Argumentos variables

```python
def suma_total(*args):
    return sum(args)


def mostrar_datos(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
```

### Alcance de variables

```python
x = 10

def f():
    x = 5   # local
    return x
```

---

## 11) Manejo de errores (`try/except`)

```python
try:
    n = int(input("Numero: "))
    print(10 / n)
except ValueError:
    print("Debes introducir un entero")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
else:
    print("Todo correcto")
finally:
    print("Fin del bloque")
```

### Lanzar errores

```python
def dividir(a, b):
    if b == 0:
        raise ValueError("b no puede ser 0")
    return a / b
```

---

## 12) Ficheros

### Lectura

```python
with open("datos.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)
```

### Escritura

```python
with open("salida.txt", "w", encoding="utf-8") as f:
    f.write("Linea 1\n")
```

### Anadir (append)

```python
with open("salida.txt", "a", encoding="utf-8") as f:
    f.write("Otra linea\n")
```

---

## 13) Programacion orientada a objetos (POO) basica

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, soy {self.nombre}"


p = Persona("Ana", 20)
print(p.saludar())
```

### Herencia

```python
class Alumno(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso
```

---

## 14) Modulos

### Crear modulo

```python
# archivo: operaciones.py

def suma(a, b):
    return a + b
```

### Importar modulo

```python
import operaciones
print(operaciones.suma(2, 3))

from operaciones import suma
print(suma(4, 5))
```

---

## 15) Comprensiones y funciones utiles

```python
nums = [1, 2, 3, 4, 5]

print(sum(nums))
print(max(nums))
print(min(nums))
print(sorted(nums, reverse=True))
print(any(n > 4 for n in nums))
print(all(n > 0 for n in nums))
```

### `zip` y `map`

```python
nombres = ["Ana", "Luis", "Marta"]
notas = [8, 6, 9]

for n, nota in zip(nombres, notas):
    print(n, nota)

cuadrados = list(map(lambda x: x * x, nums))
```

---

## 16) Ejercicios tipo examen (plantillas rapidas)

### A) Validar entrada numerica

```python
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: introduce un entero")
```

### B) Contar vocales

```python
def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    return sum(1 for c in texto if c in vocales)
```

### C) Mayor de una lista

```python
def mayor_lista(lista):
    if not lista:
        return None
    mayor = lista[0]
    for n in lista[1:]:
        if n > mayor:
            mayor = n
    return mayor
```

### D) Frecuencia de palabras

```python
def frecuencia_palabras(frase):
    d = {}
    for p in frase.lower().split():
        d[p] = d.get(p, 0) + 1
    return d
```

---

## 17) Errores tipicos que penalizan
- Olvidar `:` en `if`, `for`, `while`, `def`, `class`.
- Mala indentacion (usa 4 espacios).
- Usar `=` en vez de `==` en condiciones.
- Convertir mal `input()` (si necesitas numero, usa `int` o `float`).
- No controlar division por cero.
- Acceder a indice fuera de rango en listas.
- No cerrar fichero (solucion: `with open(...)`).

---

## 18) Mini checklist antes de entregar
- El programa ejecuta sin errores.
- Se prueban casos normales y borde.
- Mensajes de salida claros.
- Nombres de variables entendibles.
- Si piden funciones, que devuelvan (`return`) lo correcto.

---

## 19) Chuleta de sintaxis (ultra rapida)

```python
# If
if cond:
    ...
elif otra:
    ...
else:
    ...

# For
for x in iterable:
    ...

# While
while cond:
    ...

# Funcion
def nombre(arg1, arg2=0):
    return arg1 + arg2

# Try
try:
    ...
except Exception:
    ...

# Lista por comprension
nuevos = [exp for x in it if cond]

# Diccionario get
d[k] = d.get(k, 0) + 1
```

---

## 20) Ultimo consejo para examen
- Si te bloqueas, escribe primero la version simple que funcione.
- Divide en pasos pequenos: entrada -> proceso -> salida.
- Mejor codigo correcto y claro que codigo complejo incompleto.

---

## 21) Match-case (switch de Python 3.10+)

```python
opcion = int(input("Elige opcion (1-3): "))

match opcion:
    case 1:
        print("Alta")
    case 2 | 3:
        print("Consulta o baja")
    case _:
        print("Opcion no valida")
```

Cuando usarlo:
- Cuando comparas una misma variable contra varios valores fijos.
- Si solo tienes 1-2 condiciones, `if/elif` suele ser suficiente.

---

## 22) Validacion rapida de texto de entrada

```python
texto = input("Dato: ").strip()

if texto.isdigit():
    numero = int(texto)
    print("Entero valido", numero)
elif texto.isalpha():
    print("Solo letras")
elif texto.isalnum():
    print("Letras y numeros")
else:
    print("Contiene simbolos o espacios")
```

---

## 23) Expresiones regulares (regex) para examen

```python
import re

patron_telefono = r"[6-8][0-9]{8}"
telefono = "651112345"

print(bool(re.match(patron_telefono, telefono)))      # inicio
print(bool(re.search(patron_telefono, telefono)))     # en cualquier parte
print(bool(re.fullmatch(patron_telefono, telefono)))  # cadena completa
```

### Patrones frecuentes

```python
patron_letras = r"[A-Za-z]{4,8}"
patron_matricula = r"[0-9]{4}[\s-]?[B-DF-HJ-NP-TV-Z]{3}"
patron_no_579 = r"[^579]"  # cualquier caracter excepto 5, 7, 9
```

Regla de oro:
- Para validar un campo entero (telefono, dni, matricula), usa `re.fullmatch(...)`.

---

## 24) Colecciones: metodos que mas caen

### Sets (conjuntos)

```python
a = {"Ana", "Pedro", "Luis"}
b = {"Pedro", "Eva"}

print(a & b)             # interseccion
print(a | b)             # union
print(a - b)             # diferencia
print(a.intersection(b)) # metodos equivalentes
```

### Diccionarios

```python
d = {"nombre": "Ana", "edad": 20}
print(d.get("dni", "No existe"))

d.update({"activo": True, "edad": 21})
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))
```

---

## 25) Ficheros: lectura/escritura segura (texto)

```python
try:
    with open("datos.txt", "rt", encoding="utf-8") as f:
        for linea in f:
            print(linea.rstrip("\n"))
except FileNotFoundError:
    print("No existe el fichero")
except OSError as e:
    print("Error de E/S:", e)
```

### Modos de apertura que debes memorizar
- `r`: lectura (falla si no existe)
- `w`: escritura (sobrescribe)
- `a`: anade al final
- `t`: texto
- `b`: binario

---

## 26) Ficheros binarios con `pickle` (idea clave)

```python
import pickle

datos = [{"nombre": "Ana"}, {"nombre": "Luis"}]

with open("datos.bin", "wb") as f:
    pickle.dump(datos, f)

with open("datos.bin", "rb") as f:
    recuperado = pickle.load(f)

print(recuperado)
```

---

## 27) Fecha y hora (`datetime`) en 30 segundos

```python
from datetime import datetime, timedelta

ahora = datetime.now()
print(ahora.strftime("%d-%m-%Y %H:%M:%S"))

cadena = "01-03-2025 14:30"
fecha = datetime.strptime(cadena, "%d-%m-%Y %H:%M")

futura = fecha + timedelta(days=10, hours=2)
print(futura)
```

---

## 28) Iteradores (si cae teoria de objetos)

```python
nums = [10, 20, 30]
it = iter(nums)

print(next(it))
print(next(it))
print(next(it, "FIN"))
```

Idea:
- `iter(obj)` crea iterador.
- `next(it)` consume elemento a elemento.

---

## 29) POO nivel examen: `@property`, `@classmethod`, `@staticmethod`

```python
class Cuenta:
    total = 0

    def __init__(self, saldo=0):
        self._saldo = saldo
        Cuenta.total += 1

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @classmethod
    def numero_cuentas(cls):
        return cls.total

    @staticmethod
    def banco():
        return "Sucursal central"
```

---

## 30) Metodos dunder que debes reconocer

Los mas preguntables en teoria:
- `__init__`: constructor
- `__str__`: representacion en texto
- `__add__`: suma de objetos
- `__len__`: longitud
- `__iter__` y `__next__`: iteracion personalizada

Ejemplo minimo:

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
```

---

## 31) Clases abstractas (muy resumido)

```python
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
```

Idea:
- Una clase abstracta no se instancia directamente.
- Obliga a implementar metodos en las clases hijas.

---

## 32) Plantillas extras (muy utiles en examen)

### A) Quitar espacios a mano

```python
def quitar_espacios(texto):
    salida = ""
    for c in texto:
        if c != " ":
            salida += c
    return salida
```

### B) Ordenar 3 numeros sin usar `sort`

```python
def ordenar_tres(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c
```

### C) Divisores de un numero

```python
def divisores(n):
    if n <= 0:
        raise ValueError("n debe ser positivo")
    return [i for i in range(1, n + 1) if n % i == 0]
```

---

## 33) Resumen por carpetas (barrido completo)

- `.idea`: configuracion del editor (no aporta teoria de Python para examen).
- `ABURRIDO-CON-IA`: ejercicios completos de factorial, fibonacci, capicua, suma de digitos pares/impares, busqueda de posiciones, regex avanzadas, ficheros texto/binario y POO (`Pokemon`, `Nota`).
- `AprenderConIA`: dados, quiniela, pago mensual con validacion, contrasena, formato de nombre, factorial, loteria sin repetidos, conteo de palabras.
- `Boletín1-def-try-catch`: entrenamiento directo de `try/except/else/finally` con entrada por teclado.
- `Conjuntos`: union, interseccion, diferencia y metodos equivalentes.
- `Dicionarios`: `get`, `update`, `keys`, `values`, `items`, `pop`, `popitem`.
- `ejercicio`: algoritmo tipo Kaprekar y prueba de clase para tareas.
- `ejercicios-en-clases`: clases con `@property` y base abstracta.
- `Exceciones`: `assert` y captura de errores tipicos de entrada.
- `ExpresionesRegulares`: uso de `match`, `search`, `fullmatch`.
- `Fichero y Bases de Datos`: lectura y escritura de texto, binario con `pickle`.
- `FString`: formatos de decimales, porcentaje, alineacion y separador de miles.
- `Funciones`: parametros, retorno, valores por defecto, `*args`, desempaquetado.
- `hojas ejercicios`: sin contenido Python relevante.
- `Listas`: operaciones completas, matrices, `random.choice`, `sample`, `shuffle`, `enumerate`.
- `practicar`: conversion de binario a decimal con validacion.
- `Practico1EVA`: simulacion de dados hasta que todos coinciden.
- `REPASO II`: base de examenes clasicos (pares/impares, divisores, primos, ordenacion, IVA, aleatorios, bucles).
- `Teoria`: este apunte y versiones de repaso.
- `Tuplas`: conversion lista-tupla y mutabilidad interna con listas anidadas.
- `UD2Objetos`: herencia, iteradores, lambdas, clases abstractas, metodos dunder, `datetime`.
- `Validar`: validacion rapida con `isdigit` e `isalpha`.

---

## 34) Plantillas reales de ejercicios repetidos (sacadas de tus carpetas)

### A) Tirar dos dados hasta que salgan iguales

```python
import random

d1, d2 = 0, 1
intentos = 0

while d1 != d2:
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    intentos += 1

print(f"Dados: {d1} y {d2} (intentos: {intentos})")
```

### B) Tirada de N dados con M caras

```python
import random

n_dados = int(input("Numero de dados: "))
n_caras = int(input("Numero de caras: "))

if n_dados <= 0 or n_caras <= 0:
    raise ValueError("Ambos valores deben ser positivos")

tirada = [random.randint(1, n_caras) for _ in range(n_dados)]
print(tirada, "Suma:", sum(tirada))
```

### C) Quiniela (1, X, 2)

```python
import random

quiniela = []
for _ in range(15):
    r = random.randint(1, 3)
    quiniela.append("X" if r == 3 else str(r))

print(quiniela)
```

### D) Aleatorio entre dos numeros en cualquier orden

```python
import random

a = int(input("A: "))
b = int(input("B: "))

if a > b:
    a, b = b, a

print(random.randint(a, b))
```

---

## 35) Numeros: divisores y primos (version examen)

```python
def divisores(n):
    if n <= 0:
        raise ValueError("n debe ser positivo")
    return [d for d in range(1, n + 1) if n % d == 0]


def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True
```

### Primos en un rango

```python
def primos_entre(a, b):
    if a > b:
        a, b = b, a
    return [n for n in range(a, b + 1) if es_primo(n)]
```

---

## 36) Plantillas de validacion con regex (nivel practico)

### Telefono espanol con prefijo internacional

```python
import re

PATRON_TEL = r"^\+34 \d{9}$"

def telefono_valido(txt):
    txt = re.sub(r"\s+", " ", txt.strip())
    return bool(re.fullmatch(PATRON_TEL, txt))
```

### Clave de formato fijo

```python
import re

PATRON = r"^[A-Z]{2}\d{2}-[a-z]{2}[A-Z]-\d{2}$"
print(bool(re.fullmatch(PATRON, "AB12-xyZ-75")))
```

### Tarjeta + caducidad MM/YY

```python
import re

PATRON_TARJETA = r"^\d{4} \d{4} \d{4} \d{4} (0[1-9]|1[0-2])/\d{2}$"
```

---

## 37) Cadenas y texto que se repiten en tus ejercicios

### Contar palabras ignorando puntuacion

```python
import string

def contar_palabras(texto):
    for signo in string.punctuation:
        texto = texto.replace(signo, "")
    return len(texto.split())
```

### Buscar posiciones de un caracter

```python
def posiciones(texto, ch):
    return [i for i, c in enumerate(texto) if c == ch]
```

### Capicua (solo digitos)

```python
def es_capicua(txt):
    dig = "".join(c for c in txt if c.isdigit())
    return dig == dig[::-1]
```

---

## 38) Conversiones frecuentes

### Binario a decimal con control de error

```python
def binario_a_decimal(bi):
    if not bi or any(c not in "01" for c in bi):
        raise ValueError("No es binario valido")
    return int(bi, 2)
```

### Comprobar divisibilidad por 3 usando suma de digitos

```python
def divisible_entre_3(n):
    suma = sum(int(d) for d in str(abs(n)))
    return suma % 3 == 0
```

---

## 39) Alertas importantes vistas en tus propios codigos

- No uses `=` en condiciones (`if x == 3`, nunca `if x = 3`).
- Evita `except:` vacio en examen, mejor `except ValueError`, `except ZeroDivisionError`, etc.
- Si abres ficheros, usa siempre `with open(...)`.
- En primos grandes, evita probar todos los divisores hasta `n`; usa hasta raiz cuadrada.
- Si usas regex para validar un dato completo, usa `re.fullmatch(...)`.
- Si el usuario mete dos numeros en orden desconocido, normaliza con `if a > b: a, b = b, a`.

---

## 40) Mini guia de estudio final (orden recomendado para esta noche)

1. Repasar secciones 4, 5, 10, 11 (control, bucles, funciones, errores).
2. Hacer 3 ejercicios tipo: dados, divisores/primo, fichero o regex.
3. Memorizar plantillas de secciones 34, 35 y 36.
4. Dejar marcadas con buscador las palabras: `try`, `list`, `dict`, `regex`, `class`, `with open`.

---

## 41) Ejemplos de ejercicios utiles (Boletin + Examen)

Estos son ejercicios muy repetidos en tus carpetas `Boletin*` y `Examen*`.

### 1) Adivinar numero con pistas e intentos

```python
import random

objetivo = random.randint(1, 50)
fallos = 0

while True:
    intento = int(input("Adivina (1-50): "))
    if intento == objetivo:
        print(f"Acertaste. Fallaste {fallos} veces")
        break
    if intento < objetivo:
        print("Mas alto")
    else:
        print("Mas bajo")
    fallos += 1
```

### 2) Confirmar contrasena hasta que coincida

```python
clave = input("Introduce clave: ").strip()

while True:
    intento = input("Repite clave: ").strip()
    if intento == clave:
        print("Clave confirmada")
        break
    print("No coincide")
```

### 3) Factorial y Fibonacci

```python
def factorial(n):
    if n < 0:
        raise ValueError("n debe ser >= 0")
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    serie = [0, 1]
    while len(serie) < n:
        serie.append(serie[-1] + serie[-2])
    return serie
```

### 4) Capicua y suma de cifras pares/impares

```python
def es_capicua_num(n):
    s = str(abs(n))
    return s == s[::-1]


def suma_pares_impares(n):
    pares = 0
    impares = 0
    for c in str(abs(n)):
        d = int(c)
        if d % 2 == 0:
            pares += d
        else:
            impares += d
    return pares, impares
```

### 5) Divisores, primos y primos en rango

```python
def divisores(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def es_primo(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def primos_entre(a, b):
    if a > b:
        a, b = b, a
    return [x for x in range(a, b + 1) if es_primo(x)]
```

### 6) Loteria y quiniela

```python
import random

loteria = sorted(random.sample(range(1, 50), 6))
print("Loteria:", loteria)

quiniela = []
for _ in range(15):
    r = random.randint(1, 3)
    quiniela.append("X" if r == 3 else str(r))
print("Quiniela:", quiniela)
```

### 7) Convertir segundos a dias, horas, minutos, segundos

```python
segundos = int(input("Segundos: "))

dias = segundos // 86400
segundos %= 86400
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(f"{dias} dias, {horas} horas, {minutos} minutos, {segundos} segundos")
```

### 8) Contar palabras ignorando puntuacion

```python
import string

def contar_palabras(texto):
    for signo in string.punctuation:
        texto = texto.replace(signo, "")
    return len(texto.split())
```

### 9) Validacion NIF/NIE (base)

```python
import re

LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"

def nif_valido(nif):
    nif = nif.upper().strip()
    if not re.fullmatch(r"\d{8}[A-Z]", nif):
        return False
    numero = int(nif[:8])
    return LETRAS[numero % 23] == nif[-1]


def nie_valido(nie):
    nie = nie.upper().strip()
    if not re.fullmatch(r"[XYZ]\d{7}[A-Z]", nie):
        return False
    mapa = {"X": "0", "Y": "1", "Z": "2"}
    numero = int(mapa[nie[0]] + nie[1:8])
    return LETRAS[numero % 23] == nie[-1]
```

### 10) Regex de examen tipicos

```python
import re

cp_madrid = r"^28\d{3}$"
tel_es = r"^\+34 \d{9}$"
matricula = r"^\d{4}[ -]?[B-DF-HJ-NP-TV-Z]{3}$"
clave = r"^[A-Z]{2}\d{2}-[a-z]{2}[A-Z]-\d{2}$"
tarjeta = r"^\d{4} \d{4} \d{4} \d{4} (0[1-9]|1[0-2])/\d{2}$"
numero_4_8 = r"^\d{4,8}$"
```

### 11) Ficheros: comparar y procesar

```python
def comparar_ficheros(a, b):
    with open(a, "r", encoding="utf-8") as f1, open(b, "r", encoding="utf-8") as f2:
        return f1.read() == f2.read()


def alumnos_aprobados(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            nombre, notas_txt = linea.strip().split(": ")
            notas = [float(x) for x in notas_txt.split(", ")]
            if all(n >= 5 for n in notas):
                media = round(sum(notas) / len(notas), 1)
                apellido, nombre = nombre.split(", ")
                print(f"{nombre} {apellido} - {media}")
```

### 12) POO corta que puede caer (notas)

```python
class Nota:
    COLORES_VALIDOS = {"amarillo", "verde", "blanco", "cyan"}

    def __init__(self, titulo, descripcion, color="amarillo"):
        self.titulo = titulo.strip()
        self.descripcion = descripcion.strip()
        self.color = color if color in self.COLORES_VALIDOS else "amarillo"

    def crear_nota(self, titulo, descripcion, color="amarillo"):
        self.titulo = titulo.strip()
        self.descripcion = descripcion.strip()
        self.color = color if color in self.COLORES_VALIDOS else "amarillo"

    def eliminar_nota(self):
        self.titulo = ""
        self.descripcion = ""

    def listar_nota(self):
        print(f"[{self.color}] {self.titulo}: {self.descripcion}")
```

---

## 42) Mini simulacro (10 minutos)

1. Pide un numero y muestra si es primo.
2. Pide dos numeros y muestra los primos entre ambos.
3. Valida un telefono `+34 9digitos` con regex.
4. Genera una loteria de 6 numeros sin repetidos.
5. Cuenta palabras de una frase ignorando puntuacion.

Si haces estos 5 sin mirar, vas muy bien preparado.
