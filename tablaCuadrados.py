print("Ingrese la cantidad de números:")
while True:
    limite = int(input())
    if limite >= 0:
        break

k = 1
while True:
    if k <= limite:
        print(k, " ", k * k, " ", kn + k * k, sep="")
        siguiente = k + 1
    if k > limite:
        break
