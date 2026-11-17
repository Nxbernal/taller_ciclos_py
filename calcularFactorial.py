valor = int(input("Ingrese un número: "))
if valor < 0:
    print("el número no posee factorial.")
else:
    resultado = 1
    paso = 1
    while True:
        if valor > 0:
            resultado = resultado * paso
            paso = paso + 1
        if paso > valor:
            break
    print("El factorial de", valor, "es:", resultado)
