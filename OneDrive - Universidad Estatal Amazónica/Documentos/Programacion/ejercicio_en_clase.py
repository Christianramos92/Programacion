matriz = [
[6, 12, 5],
[ 6, 8, 19],
[9, 7, 3]
]
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        matriz[fila][columna]= matriz[fila][columna] * 2
        print(matriz[fila][columna],  end = "  " )
    print()