print("Bienvenido a su calculadora de área de un circulo")
print("Porfavor ingrese el radio del círculo: ")
radio = int(input())
pi = 3.1416
resultado = float(pi * (radio * radio))
print("El área del círculo es de:", round(resultado, 2), "metros cuadrado.")