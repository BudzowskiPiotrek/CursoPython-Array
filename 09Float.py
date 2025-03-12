# Almacenar en una lista los sueldos (valores float) de 5 operarios.
# Imprimir la lista y el promedio de sueldos.

lista = []
suma = 0
for x in range(5):
    valor = float(input("Ingrese un valor:"))
    suma += valor
    lista.append(valor)

promedio = suma / 5
print(lista)
print(promedio, " euros")
