import numpy as np
v1 = np.array([1, 2, 3])
v2 = np.array([-1, 1, -1])
v3 = np.array([4, -1, 1])
A = np.vstack([v1, v2, v3])
det = np.linalg.det(A)

if det != 0:
    print("Los vectores son linealmente independientes.")
else:
    print("Los vectores son linealmente dependientes.")