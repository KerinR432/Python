def cuadrado(x):
    return x**2

print(cuadrado(25))

#* ------------------- Funciones lambda ------------------

# Funciones para los enfermitos que les gusta escribir en una solo línea de codigo,
# como si mejorara el codigo o lo hicera más eficiente.
cuadradoLambda = lambda x: x**2

print(cuadradoLambda(25))

sumaLambda = lambda x,y,z: x+y+z

print(sumaLambda(12,5,6))

media = lambda *lista: sum(lista)/len(lista)

print(media(3,4,5,6,6,3,8,9))