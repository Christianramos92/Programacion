matriz = [
[6, 8, 12],
[18, 6, 8],
[9, 11, 7]
]
suma = 0
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        suma = suma + matriz[fila][columna]


print(suma)
    