print("Ingrese el máximo valor para x:")
while True:
    limiteX = int(input())
    if limiteX >= 0:
        break

t = 0
while True:
    if t <= limiteX:
        ft = t ** 3 + t ** 2 - 5
        print("Para x =", t, "f(x) =", ft)
        t = t + 2
    if t > limiteX:
        break
