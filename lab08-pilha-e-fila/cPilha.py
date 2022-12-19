from cNo import No

class Pilha:
    def __init__(self):
        self.__inicio__ = None
        self.__tamanho__ = 0

    def __str__(self):
        outStr = "-*-\n"
        no_atual = self.__inicio__
        while no_atual != None:
            outStr += str(no_atual.getDado())+'\n'
            no_atual = no_atual.getProx()
        outStr += "-*-"

        return outStr


    def empilhar(self, x):
        novo_no = No(x)
        if self.__tamanho__ == 0:
            self.__inicio__ = novo_no
            self.__tamanho__ += 1
            return
        novo_no.setProx(self.__inicio__)
        self.__inicio__ = novo_no
        self.__tamanho__ += 1
        return

    def desempilhar(self):
        if self.__tamanho__ == 0:
            return None

        antigo_topo = self.__inicio__
        novo_topo = antigo_topo.getProx()
        valor_antigo = antigo_topo.getDado()
        del antigo_topo

        self.__inicio__ = novo_topo
        self.__tamanho__ -= 1

        return valor_antigo

    def vazia(self) -> bool:
        return True if not self.__tamanho__ else False
