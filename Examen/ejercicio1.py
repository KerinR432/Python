num = int(input("Introduce un primero numero:\n"))
num2 = int(input("Introduce un segundo numero:\n"))
capicua = []
if num > num2:
    print(f"{num2} y {num}")
    for n in range(num2,num):
        capicua.append(n)

    print(f"{capicua},{num}")
else:
    print(f"{num} y {num2}")

for i in range(0,len(capicua)):
    num = capicua[i]

    if num > 9:
        if num == num:
            print(capicua[i])