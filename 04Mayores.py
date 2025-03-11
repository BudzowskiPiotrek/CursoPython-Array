# Definir por asignación una lista con 8 elementos enteros.
# Contar cuantos de dichos valores almacenan un valor superior a 100.

lista = [1, 2, 3, 4, 5, 6, 711, 811]
suma = 0

for var in lista:
    if var > 100:
        suma += 1

print(f"dentro de la lista hay {suma} de numeros mayores de 100")
