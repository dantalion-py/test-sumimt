# Partiendo del resultado obtenido en el ejercicio 25, disena una recurren-
# cia para calcular el cuadrado de cualquier n ́umero a partir del cuadrado
# del anterior. Implementa entonces la siguiente funcion recursiva, que
# devuelve el cuadrado de n:
# int cuadrado(int n)
def cuadrado(num):
    odd = 1
    sq = 0
    
    # convertir el número a positivo si es negativo
    num = abs(num)
 
    while num > 0:
        sq = sq + odd
        odd = odd + 2
        num = num - 1
 
    return sq


print(cuadrado(5))