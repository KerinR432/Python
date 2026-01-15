#* se abre el fichero, se puede manipular.

#Siempre trabajar con excepciones

"""
read = elemento String
readline = indica el nuermo de catacter que quiere que lea pero sin argumentos lee una linea entera.
readlines = lee en linea en linea
"""

try:
    # Sino ponemos nada, el fichero por defecto lo hace en modo lectura y estilo texto
    #* r = modo lectura y provoca error sino existe
    #* w = modo escritura, sino existe lo crea
    #* a = lo que hace es que aunque exista el fichero, no sobreescribe, sino que pone el texto debajo de el.
    #* || "t" es modo texto y "b" es modo binario
    fichero = open("quijote.txt","rt")
    textoRead = fichero.read() # leer fichero completo
    print(textoRead)
    fichero.close()
    print("========================")
    fichero = open("quijote.txt","rt")
    textoReadLine = fichero.readlines() # lee linea completa
    print(textoReadLine)
    fichero.close()
    print("========================")
    fichero = open("quijote.txt","rt")
    textoReadLine = fichero.readline(6) # que sea 4 caraceteres
    while textoReadLine!="":
        if textoReadLine[-1]=="\n":#Eliminamos el ultimo salto de linea sin eliminar ningun caracteer
            print(textoReadLine[:-1]) #Eliminamos todos los saltos de Lineas
        else:
            print(textoReadLine)
        textoReadLine = fichero.readline(6)
    fichero.close()
    #* se cierra el fichero y ya no se puede manipular

except :
    print("Error al manipular el fichero")


#===========================================================================================================
"""
ESCRITURA
este modo borra y empieza desde cero.
para escribir tenemos:
write escribe todo en una sola linea
writelines() funciona con una lista
"""

try:
    ficheroEscritura = open("quijote.txt","wt")
    lista = ["vivia un freddy, tan contecto como un niño","pepe"]
    ficheroEscritura.write("En algun lugar de Caracas\n")
    ficheroEscritura.write(" cuyo lugar nadie se acuerda\n")
    ficheroEscritura.writelines(lista)

    ficheroEscritura.close("Escritura")

except :
    print("Error al manipular el fichero")

#=================================================================================================================
"""
MODO APPEND
Este modo no sobre escribe ni borra, lo coloca abajo
"""

try:
    ficheroAppend = open("quijote.txt","at")
    ficheroAppend.write("En algun lugar de Caracas\n")
    ficheroAppend.write(" cuyo lugar nadie se acuerda\n")

    ficheroAppend.close("Escritura")

except :
    print("Error al manipular el fichero")

#===================================================================================================================

#a veriguar donde esta el cursor
try:
    ficherBuscarCurso = open("quijote.txt","r+")
    print(ficherBuscarCurso.read())
    print(ficherBuscarCurso.tell()) #* esto muestra donde esta el cursor imaginario
    ficherBuscarCurso.write("xxxxx")
    print(ficherBuscarCurso.read())
    print(ficherBuscarCurso.tell())
    ficherBuscarCurso.seek(0) #* Manipula el cursor, el "0" lleva al principio del ficher, "0,2" lo pone al final del ficher
                                #*con seek(n) lo colaca donde tu le indiques
    print(ficherBuscarCurso.tell())
    ficherBuscarCurso.seek(ficherBuscarCurso.tell() + 10)
    print(ficherBuscarCurso.tell())

except :
    print("Error al manipular el fichero")