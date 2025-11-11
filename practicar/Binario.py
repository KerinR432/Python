binario = input("Introduce un numero binario: ")

def decimal (bi):
    for c in bi:
        c = int(c)
        if c > 1 and c <= 9:
            return -1
    dec = int(bi, 2)
    return dec
print(decimal(binario))
