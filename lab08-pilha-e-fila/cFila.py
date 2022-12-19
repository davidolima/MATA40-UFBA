from cNo import No

class Fila:
    def __init__(self):
        self.__inicio__ = None
        self.__final__ = None
        self.__tamanho__ = 0

    def __str__(self):
        if not self.__tamanho__:
            return "< Fila Vazia >"
        outStr = "[Começo] "
        no_atual = self.__inicio__
        while no_atual != None:
            outStr += str(no_atual.getDado())+' <- '
            no_atual = no_atual.getProx()
        outStr += "[Fim]"

        return outStr


    def enfileirar(self, x):
        novo_no = No(x)
        if self.__tamanho__ == 0:
            self.__inicio__ = novo_no
            self.__final__ = novo_no
        self.__final__.setProx(novo_no)
        self.__final__ = novo_no
        self.__tamanho__ += 1
        return

    def desenfileirar(self):
        if self.__tamanho__ == 0:
            return None
        antigo_inicio = self.__inicio__
        valor_antigo = antigo_inicio.getDado()
        self.__inicio__ = self.__inicio__.getProx()
        self.__tamanho__ -= 1
        del antigo_inicio
        return valor_antigo

    def vazia(self) -> bool:
        return True if not self.__tamanho__ else False
