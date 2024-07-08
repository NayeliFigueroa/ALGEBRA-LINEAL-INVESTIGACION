import numpy as np
v1 = np.array([-1, 4])
v2 = np.array([-5, 20])
A = np.vstack([v1, v2])
det = np.linalg.det(A)

if det != 0:
  print("Los vectores son linealmente independientes.")
else:
  print("Los vectores son linealmente dependientes.")