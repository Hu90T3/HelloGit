import random
print("Hello Git")

numero_secreto = random.randint(1, 10)
intento = 0

print("Adivina el número del 1 al 10")

while True:
    intento = int(input("Tu intento: "))

    if intento == numero_secreto:
        print("🎉 ¡Adivinaste! El número era", numero_secreto)
        break
    elif intento < numero_secreto:
        print("Demasiado bajo 😅")
    else:
        print("Demasiado alto 😅")

print("Ahora accede al pin ese y ve los cambios")