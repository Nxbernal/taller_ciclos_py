entrada = int(input("digite un numero: "))

if entrada > 0:
    copia = entrada
    digito = 0
    acumulado = 0
    totalDigitos = 0
    while copia > 0:
        digito = copia % 10
        copia = copia // 10
        acumulado = acumulado + digito
        totalDigitos = totalDigitos + 1
    print("La cantidad de cifras de:", entrada, "son", totalDigitos)
    print("La sumatoria es:", acumulado)
else:
    print("El numero no es positivo")
