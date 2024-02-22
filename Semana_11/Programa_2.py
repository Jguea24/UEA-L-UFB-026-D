def sort_row(grefa, row_index):
    if row_index < 0 or row_index >= len(grefa):
        print("Índice de fila fuera de rango")
        return

    grefa[row_index] = sorted(grefa[row_index])

# Ejemplo de uso
grefa = [
    [3, 7, 2],
    [5, 1, 4],
    [9, 0, 3]
]
# Ordenar la segunda fila (índice 1)
row_index = 1

print("Matriz antes de ordenar:")
for row in grefa:
    print(row)

sort_row(grefa, row_index)

print("\nMatriz después de ordenar la fila", row_index, "en orden ascendente:")
for row in grefa:
    print(row)