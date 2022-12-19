# ##################################################
# Programa de teste para uma lista encadeada
# ##################################################

import cNo
import cLSE

import sys
import random
import math

from datetime import datetime

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

    random.seed(int(datetime.now().strftime('%H%M%S')))

    numElementos = trataLinhaDeComando()

    lista = cLSE.cLSE()

    print(str(lista))

    for i in range(numElementos):
        lista.insereNo(i*2)

    print(str(lista))
    elem = 8
    print(f"Elemento {elem} existe?", f"Sim, na posição {lista.buscaDado(elem)[1]}" if lista.buscaDado(elem) else "Não")
    print(f"Remoção do {elem}:")
    lista.removeNo(elem)
    print(str(lista))
