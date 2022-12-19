# Lab 04 - Analise de Algoritmos de Busca e Ordenação
# A partir da Classe Vetor

import random

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

            for i in range(self.numObjs):
                self.vet[i] = random.randint(0, 1000)

# *******************************************************
    def __str__(self):

        outStr = "[  "

        for i in range(self.numObjs-1):
            outStr += f'{self.vet[i]} , '

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
    def ordena(self):
        self.vet = sorted(self.vet)

    def selecao(self):
        for i in range(self.getTam()):
            for j in range(self.getTam()-1):
                if self.vet[i] < self.vet[j]:
                    self.numComp += 1
                    self.vet[j], self.vet[i] = self.vet[i], self.vet[j]
    
        self.ordenado = True

    def insercao(self):
        for i in range(1,self.getTam()):
            if self.vet[i] < self.vet[i-1]:
                self.numComp += 1
                for j in range(i,0,-1):
                    if self.vet[j] < self.vet[j-1]:
                        self.numComp += 1
                        self.vet[j], self.vet[j-1] = self.vet[j-1], self.vet[j]
                    else:
                        break

        self.ordenado = True

    def bubbleSort(self):
        while(not self.ordenado):
            for i in range(self.getTam()-1):
                if self.vet[i] > self.vet[i+1]:
                    self.numComp += 1
                    break
            else:
                self.ordenado = True        
            for i in range(self.getTam()-1):
                if self.vet[i] > self.vet[i+1]:
                    self.numComp += 1
                    self.vet[i], self.vet[i+1] = self.vet[i+1], self.vet[i]

    def quickSort(self,inicio,fim):
        if fim-inicio < 1:
            if self.vet[1] < self.vet[0]:
                self.numComp += 1
                self.vet[1],self.vet[0] = self.vet[0],self.vet[1]
            return

        if fim != self.getTam():
            self.numComp += 1
            fim +=1

        pos_pivo = inicio
        pivo = self.vet[pos_pivo]

        for i in range(inicio+1, fim):
            if self.vet[i] <= self.vet[inicio]:
                self.numComp += 1
                self.vet.insert(inicio+1, self.vet.pop(i))
                pos_pivo += 1
            else:
                self.vet.insert(pos_pivo+1, self.vet.pop(i))

        self.vet.insert(pos_pivo, self.vet.pop(inicio))

        self.quickSort(inicio, pos_pivo-1) # recursão pra esquerda
        self.quickSort(pos_pivo+1, fim-1) # recursão pra direita

    def mergeSort(self,v):
        if len(v) > 1:
            self.numComp += 1
            meio = len(v)//2
            esq = v[:meio]
            dir = v[meio:]

            self.mergeSort(esq)
            self.mergeSort(dir)

            i = 0
            j = 0
            k = 0
            while i < len(esq) and j < len(dir):
                if esq[i] < dir[j]:
                    self.numComp += 1
                    v[k] = esq[i]
                    i += 1
                else:
                    v[k] = dir[j]
                    j += 1
                k += 1

            while i < len(esq):
                v[k] = esq[i]
                i += 1
                k += 1

            while j < len(dir):
                v[k] = dir[j]
                j += 1
                k += 1
