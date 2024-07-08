import numpy as np

def es_base(S):
  A = np.array(S)
  if A.shape[0] != 4:
    return False
  determinante = np.linalg.det(A)
  if determinante == 0:
    return False
  return True
S = [(3, 1, 0, 0), (3, 2, 0, 0), (-5, 1, 0, 6),(0, 1, 0, -7)]

if es_base(S):
  print("S es una base en P3")
else:
  print("S no es una base en P3")
