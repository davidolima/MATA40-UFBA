#!/usr/bin/env python3

class No:
    def __init__(self, valor):
        self.__valor__ = valor
        self.__prox__ = None

    def __str__(self):
        out = "[" + str(self.__valor__) + "]"
        return out

    def __repr__(self):
        return self.__str__()

    def setProx(self, elem):
        assert isinstance(elem, (type(self), type(None))), f"ERRO: Próximo elemento tem que ser um Nó ou None. Recebido {type(elem)}."
        self.__prox__ = elem

    def getProx(self):
        return self.__prox__

    def setValor(self, elem:int):
        self.__valor__ = elem

    def getValor(self):
        return self.__valor__
