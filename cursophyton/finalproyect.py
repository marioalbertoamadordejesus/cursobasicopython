import random

# Definir las opciones del juego
opciones = ["piedra", "papel", "tijera"]

# Configurar el número de rondas
num_rondas = 3

# Iniciar el juego
for ronda in range(num_rondas):
    print(f"Ronda {ronda + 1}")

    # Solicitar la elección del jugador
    jugador = input("Elige piedra, papel o tijera: ").lower()

    # Generar una elección aleatoria para la computadora
    computadora = random.choice(opciones)

    print(f"La computadora elige: {computadora}")

    # Determinar el resultado de la ronda
    if jugador in opciones:
        if jugador == computadora:
            print("Empate!")
        elif (
            (jugador == "piedra" and computadora == "tijera")
            or (jugador == "papel" and computadora == "piedra")
            or (jugador == "tijera" and computadora == "papel")
        ):
            print("¡Ganaste!")
        else:
            print("La computadora gana.")
    else:
        print("Elección no válida. Elige piedra, papel o tijera.")

# Fin del juego
print("Juego terminado.")
