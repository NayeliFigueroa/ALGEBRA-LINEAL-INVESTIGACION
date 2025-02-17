import numpy as np

# Verificar si el vector pertenece al conjunto (a)
def es_subespacio_a(vec):
    a, b, c, d = vec
    return a == 2 + b

# Verificar si el vector pertenece al conjunto (b)
def es_subespacio_b(vec):
    a, b, c, d = vec
    return c == a + 2*b and d == a - 3*b

# Verificar si el vector pertenece al conjunto (c)
def es_subespacio_c(vec):
    a, b, c, d = vec
    return a == 0 and b == -d

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
conjunto_a = [(2+b, b, c, d) for b in range(-5, 6) for c in range(-5, 6) for d in range(-5, 6)]  # a == 2 + b
conjunto_b = [(a, b, a + 2*b, a - 3*b) for a in range(-5, 6) for b in range(-5, 6)]  # c == a + 2*b , d == a - 3*b
conjunto_c = [(0, -d, c, d) for c in range(-5, 6) for d in range(-5, 6)]  # a == 0 ,  b == -d

# Verificar cada conjunto
print("¿El conjunto (a) es un subespacio vectorial?", es_subespacio(conjunto_a, es_subespacio_a))
print("¿El conjunto (b) es un subespacio vectorial?", es_subespacio(conjunto_b, es_subespacio_b))
print("¿El conjunto (c) es un subespacio vectorial?", es_subespacio(conjunto_c, es_subespacio_c))