import numpy as np
v1 = np.array([2, -1, 4])
v2 = np.array([4, -2, 8])
v3 = np.array([1, 1, 1]) # no afecta el resultado
A = np.vstack([v1, v2, v3])
det = np.linalg.det(A)

if det != 0:
    print("Los vectores son linealmente independientes.")
else:
    print("Los vectores son linealmente dependientes.")