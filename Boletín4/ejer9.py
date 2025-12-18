def buscar_caracter(cadena, caracter):
    posiciones = []
    
    # Enumerar nos da el índice (i) y el valor (char) al mismo tiempo
    for i, char in enumerate(cadena):
        if char == caracter:
            posiciones.append(i)
            
    return posiciones

# Lógica principal
texto = input("Ingresa el texto: ").lower()
buscado = input("Carácter a buscar: ").lower()

if len(buscado) != 1:
    print("Error: Debes introducir exactamente UN carácter.")
else:
    resultados = buscar_caracter(texto, buscado)
    
    if resultados:
        # Convertimos la lista de números a texto separado por comas
        pos_str = ", ".join(map(str, resultados))
        print(f"La '{buscado}' aparece en {len(resultados)} ocasiones.")
        print(f"Las posiciones en las que aparece son: {pos_str}")
    else:
        print(f"La '{buscado}' no aparece en la cadena.")