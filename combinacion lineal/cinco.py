import numpy as np

def combinacion_lineal(vectores, escalares):
  if len(vectores) != len(escalares):
    raise ValueError("La cantidad de vectores debe ser igual a la cantidad de escalares.")
  
  combinacion_lineal = np.array([0, 0])
  for vector, escalar in zip(vectores, escalares):
    combinacion_lineal += escalar * np.array(vector)
  
  return combinacion_lineal

vectores = [[-2, 3], [2, 5], [3, -1]]
escalares = [3, 4, 2]

combinacion = combinacion_lineal(vectores, escalares)
print(f"Combinación lineal: {combinacion}")
