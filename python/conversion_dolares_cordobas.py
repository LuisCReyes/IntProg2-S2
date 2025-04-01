print("Porfavor digite la cantidad que desea convertir en córdobas:")


def dolares_a_cordobas(dolares, tasa_cambio):
    cordobas = dolares * tasa_cambio
    return cordobas

dolares = int(input())  
tasa_cambio = 36.49

cordobas = dolares_a_cordobas(dolares, tasa_cambio)

print(f"{dolares} dolares son {round(cordobas,2)} córdobas.")