def es_transformacion_lineal(T, u, v, c):
    if T(u + v)[0] != T(u)[0] + T(v)[0] or T(u + v)[1] != T(u)[1] + T(v)[1]:
        return False

    if T(c * u)[0] != c * T(u)[0] or T(c * u)[1] != c * T(u)[1]:
        return False

    return True

T = lambda x, y=0, z= 0: (x, y) 
u = (1, 2, 5)  
v = (3, 4, 2) 
c = 2 

if es_transformacion_lineal(T, u, v, c):
    print("La transformación T es lineal.")
else:
    print("La transformación T no es lineal.")