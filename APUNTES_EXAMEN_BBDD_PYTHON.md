# Apuntes rapidos para el examen: Python + MySQL

Este resumen esta hecho a partir de los ejercicios del repo. La idea es que puedas:

- repasar rapido antes del examen
- copiar una plantilla base y adaptarla
- entender que hace cada parte del codigo
- evitar errores tipicos

## 1. Que se esta trabajando en estos ejercicios

Los archivos del proyecto repiten siempre el mismo flujo:

1. Importar `mysql.connector`
2. Conectarse a la base de datos con `connect(...)`
3. Crear un cursor con `conexion.cursor()`
4. Ejecutar una consulta SQL con `cursor.execute(...)`
5. Leer resultados o modificar datos
6. Hacer `commit()` si hubo cambios
7. Cerrar cursor y conexion
8. Capturar errores con `mysql.connector.Error`

Si entiendes bien ese esquema, tienes casi todo el examen controlado.

## 2. Esquema mental que debes memorizar

Piensa siempre asi:

`conexion -> cursor -> execute -> fetch/recorrer -> commit si cambia -> close`

Regla rapida:

- `SELECT` lee datos
- `INSERT` inserta datos
- `UPDATE` modifica datos
- `DELETE` borra datos
- `commit()` solo hace falta cuando cambias datos

## 3. Plantilla minima para cualquier ejercicio

```python
import mysql.connector

try:
    conexion = mysql.connector.connect(
        user="daw2",
        password="LaElipa",
        host="localhost",
        database="dwes9"
    )

    cursor = conexion.cursor()

    sql = "SELECT nombre FROM pokemon"
    cursor.execute(sql)

    for fila in cursor:
        print(fila)

    cursor.close()
    conexion.close()

except mysql.connector.Error as error:
    print("Error al conectar o ejecutar la consulta:", error)
```

## 4. Conexion a la base de datos

```python
conexion = mysql.connector.connect(
    user="daw2",
    password="LaElipa",
    host="localhost",
    database="dwes9"
)
```

Que significa cada dato:

- `user`: usuario de MySQL
- `password`: contrasena del usuario
- `host`: donde esta el servidor, normalmente `localhost`
- `database`: nombre de la base de datos que quieres usar

Si la conexion falla, salta una excepcion de tipo `mysql.connector.Error`.

## 5. El cursor: para que sirve

El cursor es el objeto que ejecuta las consultas SQL.

```python
cursor = conexion.cursor()
```

Sin cursor no puedes lanzar `SELECT`, `UPDATE`, `INSERT` ni `DELETE`.

Tambien puedes usar:

```python
cursor = conexion.cursor(dictionary=True)
```

Con eso, cada fila se devuelve como diccionario:

```python
print(fila["nombre"])
```

En vez de:

```python
print(fila[0])
```

## 6. Formas de hacer un SELECT

### A. Recorrer el cursor directamente

```python
sql = "SELECT nombre FROM pokemon"
cursor.execute(sql)

for fila in cursor:
    print(fila)
```

Util cuando quieres ir mostrando resultados uno a uno.

### B. Usar `fetchall()`

```python
sql = "SELECT nombre FROM pokemon"
cursor.execute(sql)
lista_pokemons = cursor.fetchall()
print(lista_pokemons)
```

Util cuando quieres guardar todos los resultados en una lista.

### C. Seleccionar solo columnas concretas

```python
sql = "SELECT nombre, numero_pokedex FROM pokemon"
cursor.execute(sql)

for nombre, numero in cursor:
    print(numero, "-", nombre)
```

Esto es mejor que usar `SELECT *` cuando el enunciado pide datos concretos.

## 7. Clausula `WHERE`

Sirve para filtrar registros.

### Ejemplo: pokemons de mas de 1.5 de altura

```python
sql = "SELECT nombre FROM pokemon WHERE altura > 1.5"
cursor.execute(sql)

for nombre, in cursor:
    print(nombre)
```

Ojo importante:

- si el enunciado dice "solo los nombres", no deberias hacer `SELECT *`
- lo correcto es pedir solo `nombre`

## 8. `UPDATE`: modificar datos

### Ejemplo: poner en mayusculas los nombres de los pokemon con peso mayor que 200

```python
sql = "UPDATE pokemon SET nombre = UPPER(nombre) WHERE peso > 200"
cursor.execute(sql)
conexion.commit()
```

Puntos clave:

- `UPDATE` cambia datos existentes
- `SET` indica que columna modificas
- `UPPER(nombre)` convierte el texto a mayusculas
- `WHERE peso > 200` limita que filas se cambian
- sin `commit()`, el cambio puede no guardarse

## 9. `rowcount`: cuantas filas se modificaron

Si el examen te pide informar del numero de registros afectados, usa esto:

```python
sql = "UPDATE pokemon SET nombre = UPPER(nombre) WHERE peso > 200"
cursor.execute(sql)
print(cursor.rowcount, "filas modificadas")
conexion.commit()
```

Muy importante:

- `cursor.rowcount` te da el numero de filas afectadas por la ultima operacion

## 10. Diferencia entre leer y modificar

### Cuando haces un `SELECT`

- normalmente no necesitas `commit()`
- si quieres ver datos, usas `for fila in cursor` o `fetchall()`

### Cuando haces un `UPDATE`, `INSERT` o `DELETE`

- si necesitas guardar el cambio, haces `conexion.commit()`
- puedes usar `cursor.rowcount` para saber cuantas filas cambiaron

## 11. Cierre correcto de recursos

Siempre que abras cursor y conexion, cierralos.

```python
cursor.close()
conexion.close()
```

La razon es simple: liberas recursos y evitas conexiones abiertas innecesarias.

## 12. Plantilla buena para examen

Esta es la plantilla mas util para copiar y adaptar:

```python
import mysql.connector

try:
    conexion = mysql.connector.connect(
        user="daw2",
        password="LaElipa",
        host="localhost",
        database="dwes9"
    )

    cursor = conexion.cursor()

    sql = "SELECT nombre FROM pokemon WHERE altura > 1.5"
    cursor.execute(sql)

    for nombre, in cursor:
        print(nombre)

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexion' in locals():
        conexion.close()
```

Version para `UPDATE`:

```python
import mysql.connector

try:
    conexion = mysql.connector.connect(
        user="daw2",
        password="LaElipa",
        host="localhost",
        database="dwes9"
    )

    cursor = conexion.cursor()

    sql = "UPDATE pokemon SET nombre = UPPER(nombre) WHERE peso > 200"
    cursor.execute(sql)

    print("Filas modificadas:", cursor.rowcount)
    conexion.commit()

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexion' in locals():
        conexion.close()
```

## 13. Cosas que pueden preguntarte

Preguntas muy probables:

1. Como se realiza una conexion a MySQL desde Python.
2. Para que sirve un cursor.
3. Diferencia entre `SELECT *` y `SELECT nombre`.
4. Para que sirve `fetchall()`.
5. Para que sirve `WHERE`.
6. Para que sirve `UPPER(nombre)`.
7. Cuando hay que hacer `commit()`.
8. Como saber cuantas filas fueron afectadas.
9. Como cerrar correctamente cursor y conexion.
10. Como capturar errores de base de datos.

## 14. Errores tipicos que debes evitar

### Error 1: usar `SELECT *` cuando el ejercicio pide solo un campo

Mal:

```python
SELECT * FROM pokemon WHERE altura > 1.5
```

Bien:

```python
SELECT nombre FROM pokemon WHERE altura > 1.5
```

### Error 2: olvidar el `WHERE` en un `UPDATE`

Mal:

```python
UPDATE pokemon SET nombre = UPPER(nombre)
```

Eso cambia todos los pokemons.

Bien:

```python
UPDATE pokemon SET nombre = UPPER(nombre) WHERE peso > 200
```

### Error 3: olvidar `commit()`

Si haces un `UPDATE` y no llamas a `commit()`, puede que el cambio no se guarde.

### Error 4: no cerrar conexion y cursor

Siempre cierra al final.

### Error 5: imprimir mal los errores

Mejor asi:

```python
except mysql.connector.Error as error:
    print("Error:", error)
```

## 15. Truco para entender el examen rapido

Si ves un enunciado, separalo en 3 preguntas:

1. Que tabla uso.
2. Quiero leer o quiero modificar.
3. Que condicion lleva el `WHERE`.

Ejemplo:

"Muestra los nombres de los pokemons de mas de 1.5 de altura"

- tabla: `pokemon`
- accion: leer -> `SELECT`
- dato que quiero: `nombre`
- condicion: `altura > 1.5`

Resultado:

```sql
SELECT nombre FROM pokemon WHERE altura > 1.5
```

Otro ejemplo:

"Pon en mayusculas los nombres de los pokemons de mas de 200 de peso e informa del numero de registros modificados"

- tabla: `pokemon`
- accion: modificar -> `UPDATE`
- cambio: `nombre = UPPER(nombre)`
- condicion: `peso > 200`
- extra: mostrar `cursor.rowcount`

Resultado:

```sql
UPDATE pokemon SET nombre = UPPER(nombre) WHERE peso > 200
```

## 16. Chuleta express de 1 minuto

```python
import mysql.connector

try:
    conexion = mysql.connector.connect(user="daw2", password="LaElipa", host="localhost", database="dwes9")
    cursor = conexion.cursor()

    cursor.execute("SELECT nombre FROM pokemon WHERE altura > 1.5")
    for nombre, in cursor:
        print(nombre)

except mysql.connector.Error as error:
    print(error)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexion' in locals():
        conexion.close()
```

Y para modificar:

```python
cursor.execute("UPDATE pokemon SET nombre = UPPER(nombre) WHERE peso > 200")
print(cursor.rowcount)
conexion.commit()
```

## 17. Mini test para comprobar si lo sabes

Intenta responder sin mirar:

1. Que hace `cursor.execute(...)`.
2. Que diferencia hay entre `fetchall()` y recorrer `for fila in cursor`.
3. Para que sirve `commit()`.
4. Que hace `WHERE`.
5. Para que sirve `rowcount`.
6. Que ventaja tiene `dictionary=True`.
7. Que problema tiene un `UPDATE` sin `WHERE`.

Si respondes eso bien, vas preparado.

## 18. Repaso final para hoy

Haz este orden:

1. Memoriza la plantilla base.
2. Practica un `SELECT` con `WHERE`.
3. Practica un `UPDATE` con `rowcount` y `commit()`.
4. Repasa errores tipicos.
5. Intenta escribir un programa desde cero sin mirar.

## 19. Resumen final en una frase

Para aprobar este tema, tienes que dominar: conectar, crear cursor, ejecutar SQL, leer o modificar datos, guardar cambios con `commit()` cuando toque, y cerrar bien la conexion.