# #########################################
# Programa que utiliza a Classe cCor
# #########################################

import cCor
import random

if __name__ == '__main__':

    cores = []

    for i in range(100):
        cores.append(cCor.cCor( random.randint(0, 100)/100, 
                                random.randint(0, 100)/100, 
        					    random.randint(0, 100)/100) )

    for i in range(len(cores)):
        print(cores[i])
