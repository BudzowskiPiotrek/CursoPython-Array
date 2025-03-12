# Ingresar por teclado los nombres de 5 personas y almacenarlos
# en una lista. Mostrar el nombre de persona menor en orden alfabético.

lista = []

for var in range(5):
    valor = input("Ingrese el nombre:")
    lista.append(valor)
    
menor = lista[0]
posicion = 0
for x in range(1, 5):
    if lista[x] < menor:
        menor = lista[x]
        posicion = x
        
print("Menor de la lista")
print(menor)