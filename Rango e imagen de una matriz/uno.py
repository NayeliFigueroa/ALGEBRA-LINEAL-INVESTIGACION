import numpy as np

A = np.array([[1, 2],
              [3, 4]])
ref_A = np.array(A, dtype=np.float64)
rows, cols = ref_A.shape
pivot_columns = [] 
row = 0
for col in range(cols):
    if row >= rows:
        break
    if ref_A[row, col] == 0:
        nonzero_row = row + 1
        while nonzero_row < rows and ref_A[nonzero_row, col] == 0:
            nonzero_row += 1
        
        if nonzero_row < rows:
            ref_A[[row, nonzero_row]] = ref_A[[nonzero_row, row]]
    
    if ref_A[row, col] != 0:
        pivot_columns.append(col)
        for i in range(row + 1, rows):
            factor = ref_A[i, col] / ref_A[row, col]
            ref_A[i] -= factor * ref_A[row]
        
        row += 1

imagen_A = A[:, pivot_columns]
imagen_A = imagen_A.astype(int)
rango_A = len(pivot_columns)

print("Imagen de la matriz A (columnas pivote):")
for columna in imagen_A.T:
    print(columna)

print("\nRango de la matriz A:", rango_A)
