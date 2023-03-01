# Cambio de moneda. Diseñe un algoritmo recursivo que dada una
# cierta cantidad M, efect ́ue el cambio a monedas de 2, 1, 0.5, 0.2, 0.1,
# 0.05, 0.02 y 0.01 euros, devolviendo el n ́umero de monedas de cada
# tipo que constituyen el cambio (eventualmente cero para alguno de los
# tipos). Se desea que el n ́umero de monedas obtenido sea el m ́ınimo.
# Los  ́unicos operadores disponibles ser ́an los de suma y resta.


monedas = [2, 1, 0.5,0.2,0.1,0.05,0.02,0.01]
cambio = [0, 0, 0,0, 0, 0,0,0]
moneda = float(input("Introduce una cantidad entera de euros: "))
print('Para sumar', moneda, '€ se necesitan ', end='')
for i in range(len(monedas)):
    while moneda >= monedas[i]:
        moneda -= monedas[i]
        cambio[i] += 1
print(sum(cambio), 'monedas:')
for i in range(len(monedas)):
    print(cambio[i], 'monedas de ', monedas[i], '€')

