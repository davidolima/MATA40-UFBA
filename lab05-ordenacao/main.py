# Programa principal 
# Avalia o desempenho dos algoritmos de Ordenação
# Calculando o numero de comparações teórico (Complexidade)
# Com o numero de comparações efetivamente realizados pelo algoritmo

import cVetor

import sys
import random
import math

from datetime import datetime

# *******************************************************
# ***                                                 ***
# *******************************************************
def avaliaOrdenacao(vet, numTestes, funcOrdena):
    numComp     = 0
    mediaComp   = 0
    maxComp     = 0
    minComp     = 2*vet.getTam()*vet.getTam()

    for i in range(numTestes):

        if (((i+1) % 100) == 0):
            print(f'{i}...')
        else:
            vet.preencheAleatorio()

        if cVetor.__visual__:
            print(vet.vetColorRange(0, vet.getTam(), cVetor.bcolors.CRED))

        numComp = funcOrdena()

        if cVetor.__visual__:
            print(vet.vetColorRange(0, vet.getTam(), cVetor.bcolors.CGREEN))

        mediaComp += numComp

        if maxComp < numComp:
            maxComp = numComp
        if minComp > numComp:
            minComp = numComp

    mediaComp /= numTestes

    return minComp, maxComp, mediaComp

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    random.seed(int(datetime.now().strftime('%H%M%S')))

    if (len(sys.argv) > 1):
        n = int(sys.argv[1])
    else:
        n = 20

    if (len(sys.argv) > 2):
        nTestes = int(sys.argv[2])
    else:
        nTestes = n*2

    if (len(sys.argv) > 3) and (str(sys.argv[3]) == "-v" or str(sys.argv[3]) == "-V"):
        cVetor.__visual__ = True

    v = cVetor.cVetor(n)

    # minComp, maxComp, mediaComp = avaliaOrdenacao(v, nTestes, v.ordenaSelecao)

    # print(" Ordenação por Seleção ")
    # print("-----------------------")
    # print(f'# de execuções do algoritmo = {nTestes}')
    # print("=======================================================")
    # print(f'min - {minComp}     medio - {mediaComp}     max - {maxComp}')
    # print("valores teóricos:")
    # print(f'min - {n*n}     medio - {n*n}     max - {n*n}')
    # print("=======================================================")

    # minComp, maxComp, mediaComp = avaliaOrdenacao(v, nTestes, v.ordenaInsercao)

    # print(" Ordenação por Inserção ")
    # print("------------------------")
    # print(f'# de execuções do algoritmo = {nTestes}')
    # print("=======================================================")
    # print(f'min - {minComp}     medio - {mediaComp}     max - {maxComp}')
    # print("valores teóricos:")
    # print(f'min - {n}     medio - {n*n}     max - {n*n}')
    # print("=======================================================")

    # minComp, maxComp, mediaComp = avaliaOrdenacao(v, nTestes, v.ordenaBolha)

    # print(" Ordenação por Bolha ")
    # print("---------------------")
    # print(f'# de execuções do algoritmo = {nTestes}')
    # print("=======================================================")
    # print(f'min - {minComp}     medio - {mediaComp}     max - {maxComp}')
    # print("valores teóricos:")
    # print(f'min - {n}     medio - {n*n}     max - {n*n}')
    # print("=======================================================")

    minComp, maxComp, mediaComp = avaliaOrdenacao(v, nTestes, v.ordenaMerge)

    print(" Ordenação Mergesort ")
    print("---------------------")
    print(f'# de execuções do algoritmo = {nTestes}')
    print("=======================================================")
    print(f'min - {minComp}     medio - {mediaComp}     max - {maxComp}')
    print("valores teóricos:")
    print(f'min - {n*math.log2(n)}     medio - {n*math.log2(n)}     max - {n*math.log2(n)}')
    print("=======================================================")

    minComp, maxComp, mediaComp = avaliaOrdenacao(v, nTestes, v.ordenaQuick)

    print(" Ordenação Quicksort ")
    print("---------------------")
    print(f'# de execuções do algoritmo = {nTestes}')
    print("=======================================================")
    print(f'min - {minComp}     medio - {mediaComp}     max - {maxComp}')
    print("valores teóricos:")
    print(f'min - {n*math.log2(n)}     medio - {n*math.log2(n)}     max - {n*n}')
    print("=======================================================")
