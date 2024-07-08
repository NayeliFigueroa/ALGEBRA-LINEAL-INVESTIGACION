import sympy as sp
x = sp.symbols('x')
polinomio1 = 1 - x**2
polinomio2 = x
p = sp.Symbol('p')

coeficientes = [[1, 0], [-1, 1]]
matriz_coeficientes = sp.Matrix(coeficientes)

determinante = matriz_coeficientes.det()
if determinante != 0:
    es_base = True
    for coeficiente in coeficientes:
        combinacion_lineal = coeficiente[0] * polinomio1 + coeficiente[1] * polinomio2
        if not sp.simplify(combinacion_lineal - p).is_zero:
            es_base = False
            break
    
    if es_base:
        print("El conjunto {1 - x^2, x} es una base para el espacio vectorial P2.")
    else:
        print("El conjunto {1 - x^2, x} NO es una base para el espacio vectorial P2.")
else:
    print("El conjunto {1 - x^2, x} NO es una base para el espacio vectorial P2 porque los polinomios no son linealmente independientes.")
