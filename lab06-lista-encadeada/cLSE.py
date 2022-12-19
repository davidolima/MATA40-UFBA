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
    def getTamanho(self):
        return self.__numElems__

# *******************************************************
# ***                                                 ***
# *******************************************************
    def __str__(self):
        outStr = "<"
        if self.__numElems__ != 0:
            x = self.__inicio__
            while x.getProx() != None:
                outStr += str(x.getDado()) + ", "
                x = x.getProx()
            outStr += str(x.getDado())
                
        outStr += ">"
        return outStr

# *******************************************************
# ***                                                 ***
# *******************************************************
    def insereNo(self, n):
        novo = cNo.cNo(n)

        if self.__numElems__ == 0:
            self.__inicio__ = novo
            self.__numElems__ += 1
            return

        x = self.__inicio__
        while(x.getProx() != None):
            x = x.getProx()

        self.__numElems__ += 1
        x.setProx(novo)

# *******************************************************
# ***                                                 ***
# *******************************************************
    def buscaDado(self, n):
        if self.__numElems__ == 0:
            return False

        x = self.__inicio__
        indice = 0
        while (x != None):
            if (x.getDado() == n):
                return True, indice
            elif (x.getProx() == None):
                return False

            x = x.getProx()
            indice += 1

# *******************************************************
# ***                                                 ***
# *******************************************************
    def removeNo(self, n):
        if self.__numElems__ == 0:
            return False

        if self.__inicio__.getDado() == n:
            self.__inicio__ = self.__inicio__.getProx()
            return

        x = self.__inicio__
        while (x.getProx() != None and x.getProx().getDado() != n):
            x = x.getProx()

        if (x.getProx() == None):
            return False

        x.setProx(x.getProx().getProx())