# ##################################
# Calcula o fatorial de um numero n
# Algoritmo Iterativo
#         vs
# Algoritmo Recursivo
# ##################################

import sys

# *******************************************************
# ***                                                 ***
# *******************************************************
def fatorial(n):
    if n < 0:
        print("ERRO: Número negativo!")
        return None 

    print("Testando o número", n, ".")

    if n == 0:
        print("Fatorial de 0 é o problema infantil. Retornando 1.")
        return 1

    fat = 1

    for i in range(1, n+1):
        print("Retornando", fat,"*",i,".")
        fat = fat * i

    return fat

# *******************************************************
# ***                                                 ***
# *******************************************************
def fatorialRec(n):
    print("Calculando o número", n,".")
    if n == 0:
        print("Encontramos o problema infantil!")
        return 1
    print("Retornando", n,"*", n-1)
    return n * fatorialRec(n-1)

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    if (len(sys.argv) > 1):
        n = int(sys.argv[1])
    else:
        n = 6

    for i in range(n):
        print(f'O fatorial de {i} é {fatorial(i)}')
