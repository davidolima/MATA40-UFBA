# #########################################
# Programa que utiliza a Classe cPonto
# #########################################

import cPonto
import random

if __name__ == '__main__':

    ptos = []

    for i in range(100):
        pto = cPonto.cPonto(    random.randint(0, 100)/100,
                                random.randint(0, 100)/100 )
        ptos.append(pto)

    for i in range(len(ptos)):
        ptos[i].print()
