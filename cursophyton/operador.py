
print (3**2)
print(3//7)

# diferente !# 
print( 5 != 3)
print( 5 == 5)
print(3 <5)
print( 4<= 3)
print( 3<=4 )
# operador logic0 and
print("and devuelve true si los dos operandos son true ; de lo contrario, devuelve false")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print( 10 > 5 and 3<= 3)
# pedir etock mayor a 01 y menor a 90
stock = int(input("Inserte el stock "))
print(stock >= 10 and stock <=90)
# operador logico or con que uno sea verdadero, es verdadero
print("or con que uno sea verdadero, es verdadero")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
animal = input("menciona un animal")
print(animal == "gato " or animal == "perro")
#operador logico NOT invierte el resultado
print( not True)
print(not False)

print (not (True or True))
print (not(True or False))
print (not(False or True))
print (not(False or False))
#aqui lo invierte
animal = input("menciona un animal")
print(not(animal == "gato " or animal == "perro"))