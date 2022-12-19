# ##################################################
# Programa de teste para uma lista encadeada
# ##################################################

import cNo
#import cListaSimpEncadeada

import sys

# importação para gerar chaves aleatórias na lista
# ------------------------------------------------
# import random
# import math
# from datetime import datetime

# *******************************************************
# ***                                                 ***
# *******************************************************
def trataLinhaDeComando():
    n = 10
    if (len(sys.argv) > 1):
        n = int(sys.argv[1])
        if n < 0:
            n = 10
    return n

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    # inicialização no gerador de numeros aleatórios
    # -----------------------------------------------
    # random.seed(int(datetime.now().strftime('%H%M%S')))

    from cListaCircular import ListaCircular

    numElementos = trataLinhaDeComando()

    lista = ListaCircular()

    print(str(lista))

    for i in range(numElementos):
        lista.insereNo(i*2)

    print(str(lista))

    for i in range(2*numElementos):
        if lista.buscaDado(i):
            print(f'encontrei a chave {i}')
        else:
            print(f'NÃO encontrei a chave {i}')

    for i in range(5):
        if lista.removeNo(i):
            print(f'Removi a chave {i}')
        else:
            print(f'NÃO removi a chave {i}')

    print(str(lista))
    print('a')
    del lista
    print('b')
    print(str(lista))   # resulta em erro pois o objeto lista não está mais definido

