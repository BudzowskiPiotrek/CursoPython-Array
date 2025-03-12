# Definir una lista que almacene por asignación los nombres de 5 personas.
# Contar cuantos de esos nombres tienen 5 o más caracteres.

lista = ["Carla", "Beki", "Lucy", "Ana", "laiza"]
suma = 0
for var in lista:
    if len(var) >= 5:
        suma += 1

print(f"La suma de nombres que tienen 5 o mas letras son {suma}, nombres")
