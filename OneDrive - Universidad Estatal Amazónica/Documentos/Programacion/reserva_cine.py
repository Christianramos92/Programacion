#Tarea:Reserva de un asiento en sala de cine
#Estudiante: Christian Paúl Ramos Rosario
#Asignatura: Fundamentos de programación
#Paralelo:"H"
#=========================================

#Crear una matriz de 3 filas por 4 colunmas llamada asientos inicializa en 0
#(0 = asiento libre, 1 = asiento reservado)
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
print("---SALA DE CINE---")
print("Estado inicial de la sala")

for fila in range(3):
    for columna in range(4):
        print(asientos[fila][columna], end=" ")
    print() 
print("\n--- RESERVA DE ASIENTO---")

fila = int(input("Ingrese la fila (0 a 2): "))
columna = int (input("Ingrese la colunma (0 a 3): "))

if 0 <= fila <= 2 and 0 <= columna <= 3:

    if asientos[fila][columna] == 0:

       asientos[fila][columna] = 1
       print("\n¡Asientos reservadocon éxito!")
    else:   
        print("\Aviso:este asiento ya se encontraba reservado.")
else:
    print("\nError: La fila o la columnaingresada esta fuera ee rango.")

    print("\n---ESTADO FINAL DE LA SALA---")
    for fila in range(3):
        for colunma in range(4):
            print(asientos[fila][columna], end=" ")
        print()


