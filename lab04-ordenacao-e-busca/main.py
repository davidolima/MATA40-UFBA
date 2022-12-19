# Programa principal 
# Avalia o desempenho dos algoritmos de Busca
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
def avaliaBusca(vet, numBuscas, funcBusca):
    numComp     = 0
    mediaComp   = 0
    maxComp     = 0
    minComp     = vet.getTam()

    for i in range(numBuscas):

        if ((i % 1000) == 0):
            print(f'{i}...')

        chave   = random.randint(0, 1000)

        achei, pos, numComp = funcBusca(chave)

        mediaComp += numComp

        if maxComp < numComp:
            maxComp = numComp
        elif minComp > numComp:
            minComp = numComp

    mediaComp /= numBuscas

    print(f' ')

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

    v = cVetor.cVetor(n)

    minComp, maxComp, mediaComp = avaliaBusca(v, n*10, v.buscaSeq)

    print("Busca Sequencial")
    print("----------------")
    print("valores encontrados:")
    print(f'min - {minComp}     medio - {mediaComp}     max - {maxComp}')
    print("valores teóricos:")
    print(f'min - 1     medio - {n/2}     max - {n}')

    #v.ordena ()

    #v.selecao()
    #v.insercao()
    #v.bubbleSort()
    #v.quickSort(0,v.getTam())
    v.mergeSort(v.vet)
    

    v.setBuscaBinRec();


    minComp, maxComp, mediaComp = avaliaBusca(v, n*10, v.buscaBinaria)

    if v.getBuscaBinRec():
        print("Busca Binária Recursiva")
    else:
        print("Busca Binária Iterativa")
    
    print("-----------------------")
    print("valores encontrados:")
    print(f'min - {minComp}     medio - {mediaComp}     max - {maxComp}')
    print("valores teóricos:")
    print(f'min - 1     medio - {math.log2(n)}     max - {math.log2(n)}')
    print("\n--------\nVetor:", v,"\n--------\n")
