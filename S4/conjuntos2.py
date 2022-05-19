#operaciones de los conjuntos
# operadores    métodos                 descripción
# | (alt +124)  union                   Unión
# &             intersecction           Intersección
# -             difference              Diferencia
# ^             symmetric_difference    Diferencia simétrica

A = {"papa", "maiz", "trigo"}
B = {"platano", "maiz", "caña"}
C = A | B
print(A | B) # unir los 2 conjuntos
print(A.union(B)) # linea 9 y 10 son equivalentes
print(A & B)
print(A - B)
print(A ^ B)
len(C)