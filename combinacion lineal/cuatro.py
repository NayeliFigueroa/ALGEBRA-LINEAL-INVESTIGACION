import numpy as np

def es_combinacion_lineal(v, vec1, vec2, vec3):
  A = np.array([vec1, vec2, vec3]).T

  b = np.array(v)

  try:
    sol = np.linalg.solve(A, b)
  except np.linalg.LinAlgError:
    return False, None

  if np.all(np.isfinite(sol)):
    return True, sol
  else:
    return False, None

def imprimir_resultado(v, vec1, vec2, vec3, es_combinacion, coeficientes):
  if es_combinacion:
    expresion = (
        f"{coeficientes[0]} * ({vec1}) + {coeficientes[1]} * ({vec2}) "
        f"+ {coeficientes[2]} * ({vec3})"
    )
    resultado = coeficientes[0] * vec1 + coeficientes[1] * vec2 + coeficientes[2] * vec3

    print(f"Sí es una combinación lineal. Expresión: {expresion} = {resultado}")
  else:
    print("No es una combinación lineal.")

v = np.array([1, 3, -2])
vec1 = np.array([1, 1, 0])
vec2 = np.array([0, 1, 1])
vec3 = np.array([0, 0, 1])

es_combinacion, coeficientes = es_combinacion_lineal(v, vec1, vec2, vec3)

imprimir_resultado(v, vec1, vec2, vec3, es_combinacion, coeficientes)
