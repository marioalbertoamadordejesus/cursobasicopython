#crate, dead, update and delete
numeros=[1,2,3,4,5]
numeros.append(700) #agrega elementos el metodo apped
print(numeros)
numeros.insert(3, "diego")#inserta un elemento en una pocision dada
print(numeros)
tareas=["hacer uno", "hacer dos", "hacer tres"]
nueva_lista= numeros + tareas #unificar listas
print(nueva_lista)
print(nueva_lista.index("hacer dos")) #para conocer la posicion de un elemento
index= nueva_lista.index("hacer dos")
nueva_lista[index]="cambio todo" #se cambia el elemento seleccionado
print(nueva_lista)
nueva_lista.remove("hacer uno")#eliminar un elemento
print(nueva_lista)
nueva_lista.pop() #elimina el ultimo elemento de la lista
print(nueva_lista)
nueva_lista.pop(0)#elmina el elemento seleccionado segun la eleccion
print(nueva_lista)
nueva_lista.reverse()#reversa la lista
print(nueva_lista)
nuevo_orden=["la a", "el e", "anita la he", "adalaita"]
nuevo_orden.sort()#ordna de manera ordenada
print(nuevo_orden)