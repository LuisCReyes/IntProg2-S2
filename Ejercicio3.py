#Saludar
nombre = "Luis"
apellido = "Reyes"
peso = "Pesas 4lb"
edad = "y tienes 17 años"

print ("Tu nombre es:", nombre, apellido, peso, edad, sep = " ")

print ("-------------------------------------------------------------------------------")

nombre = input("Dime tu nombre: ")
edad = int(input("Dime tu edad: "))
peso = float(input("Cuánto pesas: "))
edad_dias = edad * 365
peso_kg = peso / 2.204
print("Estimado", nombre, "tu edad en días es: ", edad_dias, "y tu peso en kilogramos es: ", round (peso_kg,2), sep = " ")