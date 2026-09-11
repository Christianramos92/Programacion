matriz = [
[6, 8, 12, 6 ],
[18, 6, 8, 9] 
[9, 11, 7, 2]
]
suma = 0
cantidad = 0
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        suma = suma + matriz[fila][columna]
        cantidad = cantidad + 1
promedio = suma / cantidad
print("La suma es ", suma)
print("La cantidad es", cantidad)
print("El promedio es", promedio)        