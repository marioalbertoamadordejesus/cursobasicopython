# Ejemplo de programación funcional en Python

# Función que aplica una operación a todos los elementos de una lista
def aplicar_operacion(lista, operacion):
    return [operacion(x) for x in lista]

# Funciones de operaciones
def cuadrado(x):
    return x * x

def doble(x):
    return x * 2

def inverso(x):
    return 1 / x

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Aplicar diferentes operaciones a la lista de números
resultado_cuadrados = aplicar_operacion(numeros, cuadrado)
resultado_dobles = aplicar_operacion(numeros, doble)
resultado_inversos = aplicar_operacion(numeros, inverso)

print("Números originales:", numeros)
print("Cuadrados:", resultado_cuadrados)
print("Dobles:", resultado_dobles)
print("Inversos:", resultado_inversos)
