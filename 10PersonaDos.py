# Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
# Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.

lista = []
suma = 0
masAltas = 0

for var in range(5):
    valor = int(input("Que altura tienes: "))
    lista.append(valor)
    suma += valor

promedio = suma / 5

for var in lista:
    if var > promedio:
        masAltas += 1

masBajas = 5 - masAltas
print(promedio, " - promedio")
print(f"hay {masAltas} personas mas altas que promedio")
print(f"hay {masBajas} personas mas najas que promedio")