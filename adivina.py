# Crea un programa que radomice una serie de numeros entre 1 y 99 para que el usuario adivine cual es en un numero limitado de intentos.

from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1, 100)
nombre = input("Dime tu nombre: ")

print(f"Bueno {nombre}, he pensado en un numero entre 1 y 100 \n Tienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Cual es el numero?: "))
    intentos += 1
    #intentos = intentos +1
    
    if estimado < numero_secreto:
        print("Mi numero es mas alto")
    elif estimado > numero_secreto:
        print("Mi numero es mas bajo")
    else:
        print(f"Felicidades {nombre}! Has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento, se han agotado los intentos, El numero secreto era {numero_secreto}")
    
    