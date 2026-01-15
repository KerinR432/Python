#Para trabajar con Binarios necesitamos pickle
import pickle
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

persona1 =  Persona("Mohamed")
persona2 =  Persona("Feddy")
try:
    ficheroBinario = open("quijoteBinario.bin", "wb")
    pickle.dump(persona1, ficheroBinario) #* asi como introducimos la clases aun fichero.
    pickle.dump(persona2, ficheroBinario)
    ficheroBinario.close()


except:
    print("El archivo no existe")

#=====================================================================================================================
"""
Vamos a leer un fichero binario
"""
try:
    ficheroBinario = open("quijoteBinario.bin", "rb")
    personaLee1 = pickle.load(ficheroBinario) #* load recupera cosas
    personaLee2 = pickle.load(ficheroBinario)
    print(personaLee1.nombre) #* mostramos lo que recuperamos
    print(personaLee2.nombre)
    ficheroBinario.close()


except:
    print("El archivo no se pude leer")

#=====================================================================================================================
"""
Vamos a leer de lista completa, asi cmo escribir
"""
try:
    ficheroBinario = open("quijoteBinario.bin", "wb")
    listaEscribir = []
    listaEscribir.append(persona1) #* De una lista se puede leer,de la mejor forma
    listaEscribir.append(persona2)
    pickle.dump(listaEscribir, ficheroBinario)
    ficheroBinario.close()

    ficheroBinarioLeer = open("quijoteBinario.bin", "rb")
    l = pickle.load(ficheroBinarioLeer)

    for elemento in l: #* recuperamos una lista
        print(elemento.nombre)
    ficheroBinarioLeer.close()

except:
    print("El archivo no se pude leer")