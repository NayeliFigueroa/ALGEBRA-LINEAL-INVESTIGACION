import numpy as np

def es_base(S):
  A = np.array(S)
  if A.shape[0] != 4:
    return False
  determinante = np.linalg.det(A)
  if determinante == 0:
    return False
  return True
S = [(0, 0, 0, 1), (0, 0, 1, 1), (0, 1, 0, 1), (1, 0, 0, 1)]

if es_base(S):
  print("S es una base en P3")
else:
  print("S no es una base en P3")
