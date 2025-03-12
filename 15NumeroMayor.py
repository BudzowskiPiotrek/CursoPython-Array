# Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje
# si se repite dentro de la lista (es decir si dicho valor se encuentra en 2
# o más posiciones en la lista)

lista = []

for x in range(5):
    valor = int(input("Ingrese valor:"))
    lista.append(valor)
    
mayor = lista[0]

for x in range(1, 5):
    if lista[x] > mayor:
        mayor = lista[x]

for x in range(1, 5):
    if lista[x] == mayor:
        print(f"{mayor}, el mayor se repite")
        break

print(f"el mayor es: {mayor}")    