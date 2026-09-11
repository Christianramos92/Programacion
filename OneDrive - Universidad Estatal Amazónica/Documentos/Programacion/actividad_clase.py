matriz = [
[6, 8, 12, 5],
[18, 6, 8, 19],
[9, 11, 7, 3],
[3, 1, 4, 9]
]
for fila in range(len(matriz)):
    suma=0
    for columna in range(len(matriz[fila])):
        suma=suma+matriz[fila][columna]
    print("La suma de la fila: ", fila+1," = ",suma)
 