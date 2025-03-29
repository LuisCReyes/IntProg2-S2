print("Bienvenido 😊!")
print("Porfavor ingresa un número: ")

def antecesor_y_sucesor(numero):
    antecesor = numero - 1
    sucesor = numero + 1
    return antecesor, sucesor
    
numero = int(input())
ante, suce = antecesor_y_sucesor(numero)
print(f"El antecesor del número {numero} es {ante}")
print(f"El sucesor del número {numero} es {suce}")