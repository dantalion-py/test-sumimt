# Dise ̃nar un algoritmo recursivo que, dado un natural x y un vector
# v con n naturales, determine si x es igual a la suma de todas las
# componentes del vector. El perfil de la funci ́on debe ser el siguiente, y
# no se pueden utilizar par ́ametros auxiliares.
# int es_suma_comp(int vector[], int tam_vector, int x);




def sumalista(n):
    if len(n) == 1:
        return n[0]
    else:
        return n[0] + sum(n[1:])
    

def comparacionVertor(vector, tam_vector, x):
    suma = sumalista(vector)
    if suma > x:
        print(f"la suma del array es mayor a {x}")
    
    else:
        print(f"la suma del array es menor a {x}")
    


arr =[1,2,3,4,5]
log_array = len(arr)
comparacionVertor(arr,log_array,10)






# def comparacionVertorV2(vector, tam_vector, x):
#     for i in range(tam_vector):
#         suma +=  vector[i]
    

# arr =[1,2,3,4,5]
# log_array = len(arr)
# comparacionVertorV2(arr,log_array,10)