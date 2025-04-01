print("Porfavor digite la cantidad que desea convertir en dólares:")


def cordobas_a_dolares(cordobas, tasa_cambio):
    dolares = cordobas * tasa_cambio
    return dolares

cordobas = int(input())  
tasa_cambio = 0.027

dolares = cordobas_a_dolares(cordobas, tasa_cambio)

print(f"{cordobas} córdobas son {round(dolares,2)} dólares.")