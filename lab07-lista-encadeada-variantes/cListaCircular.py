import cNo

class ListaCircular:
    def __init__(self):
        self.__inicio__ = None
        self.__numElems__ = 0

    def __del__(self):
        noCorrente = self.__inicio__

        while noCorrente.getProx() is not None:
            aux = noCorrente
            noCorrente = noCorrente.getProx()
            aux.setProx(None)
            del aux
            self.__numElems__ -= 1

    def getTamanho(self):
        return self.__numElems__

    def __str__(self):
        outStr = ""

        noCorrente = self.__inicio__

        if noCorrente == None:
            outStr += "=====================\n"
            outStr += "|   LISTA   VAZIA   |\n"
            outStr += "=====================\n"
        else:
            while noCorrente.getProx() != self.__inicio__:
                outStr += str(noCorrente)
                noCorrente = noCorrente.getProx()
            outStr += str(noCorrente.getProx())
        return outStr

    def insereNo(self, n):
        novoNo = cNo.cNo(n)

        if self.__inicio__ == None:
            self.__inicio__ = novoNo
            novoNo.setProx(novoNo)

        else:
            noCorrente = self.__inicio__

            while noCorrente.getProx() != self.__inicio__:
                noCorrente = noCorrente.getProx()

            novoNo.setProx(self.__inicio__)
            noCorrente.setProx(novoNo)

            self.__numElems__ += 1

    def buscaDado(self, n):
        if self.__inicio__ == None:
            return False

        noCorrente = self.__inicio__

        while noCorrente != self.__inicio__ and noCorrente.getDado() != n:
            noCorrente = noCorrente.getProx()

        if noCorrente == None:
            return False

        return True

    def removeNo(self, n):
        if self.__inicio__ == None:
            return False

        no_atual = self.__inicio__

        while (no_atual.getProx().getDado() != n and no_atual.getProx() != self.__inicio__):
            no_atual = no_atual.getProx()

        if (no_atual.getProx().getDado() == n):
            antigo = no_atual.getProx()

            if antigo == self.__inicio__:
                self.__inicio__ = antigo.getProx()

            no_atual.setProx(antigo.getProx())
            self.__numElems__ -= 1

            return True
        return False
