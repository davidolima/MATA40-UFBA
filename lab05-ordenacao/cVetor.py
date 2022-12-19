# Lab 05 - Analise dos Algoritmos de Ordenação
# A partir da Classe Vetor

import random

__visual__ = False

class bcolors:
    CEND        = '\33[0m'
    CBOLD       = '\33[1m'
    CITALIC     = '\33[3m'

    CBLACK      = '\33[30m'
    CRED        = '\33[31m'
    CGREEN      = '\33[32m'
    CYELLOW     = '\33[33m'
    CBLUE       = '\33[34m'
    CMAGENTA    = '\33[35m'
    CCYAN       = '\33[36m'
    CWHITE      = '\33[37m'

# *******************************************************
# ***                                                 ***
# *******************************************************
class cVetor:

# *******************************************************
    def __init__(self, n):

        self.numObjs        = 0
        self.ordenado       = False
        self.buscaBinRec    = False
        self.numComp        = 0

        if n < 1:
            self.vet = []
        else:
            self.vet        = [0] * n
            self.numObjs    = n

        self.preencheAleatorio()

# *******************************************************
    def preencheAleatorio(self):

        for i in range(self.numObjs):
            self.vet[i] = random.randint(0, 1000)

# *******************************************************
    def getTam(self):
        return self.numObjs

# *******************************************************
    def setBuscaBinRec(self):
        self.buscaBinRec = True

# *******************************************************
    def getBuscaBinRec(self):
        return self.buscaBinRec

# *******************************************************
    def resetBuscaBinRec(self):
        self.buscaBinRec = False

# *******************************************************
    def troca(self, i, j):
        aux             = self.vet[i]
        self.vet[i]     = self.vet[j]
        self.vet[j]   = aux

# *******************************************************
    def __str__(self):

        outStr = "[  "

        for i in range(self.numObjs-1):
            outStr += f'{self.vet[i]} , '

        outStr += f'{self.vet[self.numObjs-1]} ]'

        return outStr

# *******************************************************
    def vetColorRange(self, i, f, cor):

        outStr = "[  "

        for k in range(self.numObjs-1):
            if (k >= i) and k <= f:
                outStr += f'{cor}{self.vet[k]}{bcolors.CEND} , '
            else:
                outStr += f'{self.vet[k]} , '

        if self.numObjs-1 >= i and self.numObjs-1 <= f:
            outStr += f'{cor}{self.vet[self.numObjs-1]}{bcolors.CEND} ]'
        else:
            outStr += f'{self.vet[self.numObjs-1]} ]'

        return outStr

# *******************************************************
    def vetColorKeyPair(self, k, p, cor0, cor1):

        outStr = "[  "

        for i in range(self.numObjs-1):
            if i == k:
                outStr += f'{cor0}{self.vet[i]}{bcolors.CEND} , '
            elif i == p:
                outStr += f'{cor1}{self.vet[i]}{bcolors.CEND} , '
            else:
                outStr += f'{self.vet[i]} , '

        if self.numObjs-1 == k:
            outStr += f'{cor0}{self.vet[self.numObjs-1]}{bcolors.CEND} ]'
        elif self.numObjs-1 == p:
            outStr += f'{cor1}{self.vet[self.numObjs-1]}{bcolors.CEND} ]'
        else:
            outStr += f'{self.vet[self.numObjs-1]} ]'

        return outStr

# *******************************************************
    def buscaSeq(self, chave):
        self.numComp = 0
        for i in range(self.numObjs):
            self.numComp += 1
            if self.vet[i] == chave:
                return True, i, self.numComp
        return False, -1, self.numComp

# *******************************************************
    def buscaBinariaIter(self, chave):
        self.numComp    = 0
        inicio          = 0
        fim             = self.numObjs-1

        while inicio <= fim:
            medio = int((inicio + fim) / 2)
            self.numComp += 1

            if self.vet[medio] == chave:
                return True, medio, self.numComp

            if self.vet[medio] > chave:
                fim = medio - 1
            else:
                inicio = medio + 1

        return False, -1, self.numComp

# *******************************************************
    def buscaBinariaRec(self, chave, inicio, fim):
        achei   = False
        pos     = -1

        if inicio > fim:
            return achei, pos

        medio = int((inicio + fim) / 2)
        self.numComp += 1

        if self.vet[medio] == chave:
            achei   = True
            pos     = medio
        else:
            if self.vet[medio] > chave:
                fim = medio - 1
            else:
                inicio = medio + 1

            achei, pos = self.buscaBinariaRec(chave, inicio, fim)

        return achei, pos

# *******************************************************
    def buscaBinaria(self, chave):
        self.numComp    = 0
        achei           = False
        pos             = -1

        if self.ordenado:
            if self.buscaBinRec:
                achei, pos = self.buscaBinariaRec(chave, 0, self.numObjs-1)
            else:
                achei, pos, self.numComp = self.buscaBinariaIter(chave)

        return achei, pos, self.numComp
 
# *******************************************************
    def ordenaSelecao(self):
        self.numComp = 0

        for i in range(self.numObjs):
            min = i
            for j in range(i+1, self.numObjs):

                if __visual__:
                    print(self.vetColorKeyPair(j, min, bcolors.CMAGENTA, bcolors.CCYAN))

                self.numComp += 1

                if (self.vet[min] > self.vet[j]):
                    min = j

                    if __visual__:
                        print(self.vetColorKeyPair(j, min, bcolors.CCYAN, bcolors.CMAGENTA))

            self.troca(i, min)

            if __visual__:
                print(self.vetColorKeyPair(i, min, bcolors.CCYAN, bcolors.CMAGENTA))

        self.ordenado = True

        return self.numComp

# *******************************************************
    def ordenaInsercao(self):
        self.numComp = 0

        for i in range(self.numObjs):
            j       = i
            troca   = True

            while j > 0 and troca :
                self.numComp += 1

                if __visual__:
                    print(self.vetColorKeyPair(j-1, j, bcolors.CMAGENTA, bcolors.CCYAN))

                if (self.vet[j-1] > self.vet[j]):
                    self.troca(j-1, j)

                    if __visual__:
                        print(self.vetColorKeyPair(j-1, j, bcolors.CCYAN, bcolors.CMAGENTA))

                else:
                    troca = False
                j -=1

        self.ordenado = True

        return self.numComp

# *******************************************************
    def ordenaBolha(self):
        self.numComp = 0
        troca   = True
        i       = 0

        while (troca) and (i < self.numObjs):
            troca = False

            for j in range(i, self.numObjs-1):
                self.numComp += 1

                if __visual__:
                    print(self.vetColorKeyPair(j, j+1, bcolors.CMAGENTA, bcolors.CCYAN))

                if (self.vet[j] > self.vet[j+1]):
                    troca = True
                    self.troca(j, j+1)

                    if __visual__:
                        print(self.vetColorKeyPair(j, j+1, bcolors.CCYAN, bcolors.CMAGENTA))

        self.ordenado = True

        return self.numComp

# *******************************************************
    def ordenaMerge(self):

        self.numComp = 0

        self.mergeSort(0, self.numObjs-1)

        self.ordenado = True
        
        return self.numComp

# *******************************************************
    def mergeSort(self, i, f):

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # Aqui voce deve implementar o seu método de MERGESORT
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        return

# *******************************************************
    def ordenaQuick(self):

        self.numComp = 0

        self.quickSort(0, self.numObjs-1)

        return self.numComp

# *******************************************************
    def quickSort(self, i, f):

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # Aqui voce deve implementar o seu método de QUICKSORT
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        return
