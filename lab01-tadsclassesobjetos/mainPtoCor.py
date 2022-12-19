# #########################################
# Programa que utiliza as Classes  
# cPontoCor e cCor
# #########################################

import cCor
import cPontoColorido
import random

if __name__ == '__main__':

    ptos = []

    for i in range(100):
        cor = cCor.cCor(	random.randint(0, 100)/100, 
        					random.randint(0, 100)/100, 
        					random.randint(0, 100)/100)

        pto = cPontoColorido.cPontoCor(  random.randint(0, 100)/100,
                                        random.randint(0, 100)/100, 
                                        cor)
        ptos.append(pto)

    for i in range(len(ptos)):
        print(str(ptos[i]))
