perros={
"genero" :"canino",
"canino" :"del bosque",
"antigurdad" :"2mil años"
}
perros["tu mascota se llama"] = "diego"
perros["algunas razas de perros son"] = ("chihuahuas" , "pugs" , "mestizos")
print(perros)
del perros["tu mascota se llama"]
print(perros)
genero = perros.get("genero") #lo usamos para saber si esta algo
print("Genero:", genero)