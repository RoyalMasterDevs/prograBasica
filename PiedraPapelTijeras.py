# Piedra papel y tijeras

import random

# fUNCION QUE PIDE LA ELECCION DEL JUGADOR
def eleccion_jugador():
    print("\nElige la opcion: ")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    opcion = int(input("Tu eleccion es (1-3): "))
    if opcion == 1:
        return "piedra"
    elif opcion == 2:
        return "papel"
    elif opcion == 3:
        return "tijera"

    else:
        print("Opcion invalida, elige de nuevo")
        return eleccion_jugador()
    
# Funcion que genera la eleccion de la computadora
def eleccion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

# Funcion que determina el ganador
def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "Empate"
    elif (jugador == "piedra" and computadora == "tijera") or \
        (jugador == "papel" and computadora == "piedra") or \
        (jugador == "tijera" and computadora == "papel"):
        return "Ganaste!"
    else: 
        return "Perdiste"
# Funcion principal del juego
def jugar():
    print("=== Piedra, Papel o tijera ===")
    jugador = eleccion_jugador()
    computadora = eleccion_computadora()
    print(f"Tu elegiste : {jugador}")
    print(f"La computadora eligio: {computadora}")
    print(determinar_ganador(jugador, computadora))
    
jugar()

    
