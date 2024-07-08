import numpy as np

def es_combinacion_lineal(vector, vectores):
  matriz_vectores = np.array(vectores)
  try:
    coeficientes = np.linalg.solve(matriz_vectores, vector)
    return np.all(np.isfinite(coeficientes))
  except np.linalg.LinAlgError:
    return False

vector = np.array([2, -2, 3])
vectores = [np.array([1, 2, -3]), np.array([-1, 1, 1]), np.array([-1, 4, -1])]

if es_combinacion_lineal(vector, vectores):
  print(f"El vector {vector} es combinación lineal de los vectores {vectores}")
else:
  print(f"El vector {vector} NO es combinación lineal de los vectores {vectores}")
