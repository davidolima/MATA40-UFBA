# ############################################################
# Classe que implementa uma Lista Simplesmente Encadeada - LSE
# ############################################################

import cNo

# *******************************************************
# ***                                                 ***
# *******************************************************
class cLSE:

# *******************************************************
# ***                                                 ***
# *******************************************************
    def __init__(self):
        self.__inicio__     = None
        self.__numElems__   = 0

# *******************************************************
# ***                                                 ***
# *******************************************************
    def __del__(self):

        noCorrente = self.__inicio__

        while noCorrente != None:
            aux         = noCorrente
            noCorrente  = noCorrente.getProx()
            del aux
            self.__numElems__ -= 1

# *******************************************************
# ***                                                 ***
# *******************************************************
    def getTamanho(self):
        return self.__numElems__

# *******************************************************
# ***                                                 ***
# *******************************************************
    def __str__(self):

        outStr = ""

        noCorrente = self.__inicio__

        if noCorrente == None:        
            outStr += "=====================\n"
            outStr += "|   LISTA   VAZIA   |\n"
            outStr += "=====================\n"
        else:
            while noCorrente != None:
                outStr += str(noCorrente)
                noCorrente = noCorrente.getProx()
        return outStr

# *******************************************************
# ***                                                 ***
# *******************************************************
    def insereNo(self, n):

        novoNo = cNo.cNo(n)

        if self.__inicio__ == None:
            self.__inicio__ = novoNo
        else:
            noCorrente = self.__inicio__
            
            while noCorrente.getProx() != None:
                noCorrente = noCorrente.getProx()

            noCorrente.setProx(novoNo)
            self.__numElems__ += 1

# *******************************************************
# ***                                                 ***
# *******************************************************
    def buscaDado(self, n):

        if self.__inicio__ == None:
            return False

        noCorrente = self.__inicio__
        
        while noCorrente != None and noCorrente.getDado() != n:
            noCorrente = noCorrente.getProx()

        if noCorrente == None:
            return False

        return True

# *******************************************************
# ***                                                 ***
# *******************************************************
    def removeNo(self, n):

        if self.__inicio__ == None or (not self.buscaDado(n)):
            return False

        noCorrente = self.__inicio__
        noAnterior = None
        
        while noCorrente.getDado() != n:
            noAnterior = noCorrente
            noCorrente = noCorrente.getProx()

        if noAnterior == None:      # remoção da cabeça da lista
            self.__inicio__ = noCorrente.getProx()
        else:
            noAnterior.setProx(noCorrente.getProx())

        del noCorrente
        self.__numElems__ -= 1

        return True
