import numpy as np

B = np.array([[-2, -3], [-3, -2]])
P_inversa = np.linalg.inv(B) 
def cambio_base(vector, base, inversa):
  coordenadas_nuevas = np.dot(inversa, vector)
  return coordenadas_nuevas
x= 1
y=2
vector_original = np.array([x, y])

coordenadas_nuevas = cambio_base(vector_original, B, P_inversa)

print(f"Coordenadas en la nueva base: {coordenadas_nuevas}")
