#!/usr/bin/env python3

from cNo import No

class Fila:
    def __init__(self, *elems):
        self.__inicio__ = None
        self.__final__ = None
        self.__tamanho__ = 0

        for elem in elems:
            self.inserir(elem)

    def vazia(self):
        return True if not self.__tamanho__ else False

    def getTamanho(self):
        return self.__tamanho__

    def esvaziar(self):
        while not self.vazia():
            self.remover()

    def __str__(self):
        if self.vazia():
            return "[Fila Vazia]"
        out = "<-"
        no_atual = self.__inicio__
        while no_atual != self.__final__:
            out += str(no_atual) + '<-'
            no_atual = no_atual.getProx()
        out += str(no_atual) + "<-"
        return out

    def __repr__(self):
        return self.__str__()

    def inserir(self, elem):
        novo_no = No(elem)
        if self.vazia():
            self.__final__ = novo_no
            self.__inicio__ = novo_no

        ultimo_no = self.__final__
        ultimo_no.setProx(novo_no)
        self.__final__ = novo_no

        self.__tamanho__ += 1

    def mesclar(self, fila):
        """Mesclar duas filas."""
        no_atual = fila.__inicio__
        while no_atual != fila.__final__:
            self.inserir(no_atual.getValor())
            no_atual = no_atual.getProx()
        self.inserir(fila.__final__.getValor())

    def remover(self):
        if self.vazia():
            return

        atual_inicio = self.__inicio__
        novo_inicio = atual_inicio.getProx()

        atual_inicio.setProx(None) # Remove ponteiro para o atual inicio
        valor = atual_inicio.getValor()
        del atual_inicio

        self.__inicio__ = novo_inicio

        self.__tamanho__ -= 1

        return valor

    def removerEsp(self, elem):
        """
        Remover paciente específico.
        Remove um paciente do meio da fila, que precisa ser locomovido.
        """
        if self.__inicio__ is None or self.vazia():
            return
        
        if self.__final__.getValor() == elem:
            no_atual = self.__inicio__
            while no_atual.getProx() != self.__final__ and no_atual.getProx() is not None:
                no_atual = no_atual.getProx()
            no_atual.setProx(None)
            del self.__final__
            self.__final__ = no_atual
            self.__tamanho__ -= 1
            return
        elif self.__inicio__.getValor() == elem:
            sucessor = self.__inicio__.getProx()
            self.__inicio__.setProx(None)
            del self.__inicio__
            self.__inicio__ = sucessor
            self.__tamanho__ -= 1
            return


        no_atual = self.__inicio__

        while no_atual.getProx().getValor() != elem:
            no_atual = no_atual.getProx()

        a_rmv = no_atual.getProx()
        sucessor = a_rmv.getProx()
        no_atual.setProx(sucessor)
        a_rmv.setProx(None)
        del a_rmv

        self.__tamanho__ -= 1

if __name__ == "__main__":
    f = Fila(1,2,3)
    g = Fila(7,8,9)
    f.inserir(4)
    print(f)
    f.removerEsp(1)
    f.removerEsp(3)
    print(f)
    f.removerEsp(4)
    print(f)

    f.mesclar(g)
    print(f)
