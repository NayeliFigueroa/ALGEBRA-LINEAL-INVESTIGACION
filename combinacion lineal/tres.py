import numpy as np

def es_combinacion_lineal(v, vec1, vec2):
    A = np.array([vec1, vec2]).T
    b = np.array(v)
    try:
        sol = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        return False, None
    if np.all(np.isfinite(sol)):
        return True, sol
    else:
        return False, None
def imprimir_resultado(v, vec1, vec2, es_combinacion, coeficientes):
    if es_combinacion:
        expresion = f"{coeficientes[0]} * ({vec1}) + {coeficientes[1]} * ({vec2})"
        resultado = coeficientes[0] * vec1 + coeficientes[1] * vec2
        
        print(f"Sí es una combinación lineal. Expresión: {expresion} = {resultado}")
    else:
        print("No es una combinación lineal.")

v = np.array([1, 2])
vec1 = np.array([-2, 3])
vec2 = np.array([1, -1])

es_combinacion, coeficientes = es_combinacion_lineal(v, vec1, vec2)

imprimir_resultado(v, vec1, vec2, es_combinacion, coeficientes)
