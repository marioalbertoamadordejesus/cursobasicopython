import random

numero_secreto = random.randint(1, 10)  # Genera un número secreto entre 1 y 10
intentos = 0  # Inicializa el contador de intentos

while True:  # ¡Este ciclo se ejecutará siempre!
    adivina = int(input("Adivina el número (entre 1 y 10): "))
    intentos += 1  # Aumenta el contador de intentos en 1
    
    if adivina == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break  # Termina el ciclo while
    else:
        print("Intenta de nuevo.")
