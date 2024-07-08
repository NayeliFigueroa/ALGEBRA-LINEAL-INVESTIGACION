import numpy as np

# Verificar si el vector pertenece al conjunto (a)
def es_subespacio_a(vec):
    a, b, c, d = vec
    return a == b == 0

# Verificar si el vector pertenece al conjunto (b)
def es_subespacio_b(vec):
    a, b, c, d = vec
    return a == 1 and b == 0 and c == 1 -d

# Verificar si el vector pertenece al conjunto (c)
def es_subespacio_c(vec):
    a, b, c, d = vec
    return a > 0 and b < 0

# Verificar si un conjunto es un subespacio vectorial de R^3
def es_subespacio(conjunto, verificador):
    if len(conjunto) == 0:
        return False  # Si el conjunto está vacío, no es un subespacio

    for vec in conjunto:
        if not verificador(vec):
            return False
    
    # Verificar si contiene el vector cero
    if not verificador((0, 0, 0, 0)):
        return False

    return True

# Conjunto de prueba
conjunto_a = [(0, 0, c, d) for c in range(-5, 6) for d in range(-5, 6)]  # a == b == 0
conjunto_b = [(1, 0, 1 -d, d) for d in range(-5, 6)]  # a == 1, b == 0, c == 1 -d
conjunto_c = [(a>0, b<0, c, d) for a in range(-5, 6) for b in range(-5, 6) for c in range(-5, 6) for d in range(-5, 6)]  # a == 0 ,  b == -d

# Verificar cada conjunto
print("¿El conjunto (a) es un subespacio vectorial?", es_subespacio(conjunto_a, es_subespacio_a))
print("¿El conjunto (b) es un subespacio vectorial?", es_subespacio(conjunto_b, es_subespacio_b))
print("¿El conjunto (c) es un subespacio vectorial?", es_subespacio(conjunto_c, es_subespacio_c))