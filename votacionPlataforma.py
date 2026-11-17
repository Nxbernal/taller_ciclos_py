contAndroid = 0
contIOS = 0
contNulos = 0
while True:
    print("Ingrese su código:")
    idVotante = int(input())
    if idVotante != 0:
        print("Ingrese su elección (Android / iOS):")
        opcion = input()
        opcion = opcion
        if opcion == "android":
            contAndroid = contAndroid + 1
        else:
            if opcion == "ios":
                contIOS = contIOS + 1
            else:
                print("el voto no se tendrá en cuenta.")
                contNulos = contNulos + 1
    if idVotante == 0:
        break

print("Votos Android:", contAndroid)
print("Votos iOS:", contIOS)
print("Votos no válidos (no contados):", contNulos)

if contAndroid > contIOS:
    print("La plataforma elegida es: Android")
else:
    if contIOS > contAndroid:
        print("La plataforma elegida es: iOS")
    else:
        print("Hay empate: se debe usar otro mecanismo de elección.")
