# Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados
# (4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar
# los sueldos de los empleados agrupados en dos listas. Imprimir las dos listas de sueldos.

listaTarde = []
listaManana = []

for var in range(8):
    opcion = 0
    opcion = int(input("Escribe 1 para turno de mañana y 2 para turno de tarde"))
    if opcion == 1:
        sueldo = int(input("Cual es tu sueldo"))
        listaManana.append(sueldo)
    elif opcion == 2:
        sueldo = int(input("Cual es tu sueldo"))
        listaTarde.append(sueldo)
    else:
        print("te has equivocado")
        var -= 1

print(listaManana)
print(listaTarde)
