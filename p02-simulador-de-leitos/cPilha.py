#!/usr/bin/env python3

class Pilha:
    def __init__(self):
        self.__pilha__ = []

    def empilhar(self, elem):
        self.__pilha__.append(elem)

    def desempilhar(self):
        return self.__pilha__.pop()

    def vazia(self) -> bool:
        return True if not self.__pilha__ else False

    def __str__(self):
        if self.vazia():
            return "| Pilha Vazia |"
        out = "|"
        for i in range(len(self.__pilha__)-1, -1, -1):
            if i == (len(self.__pilha__)-1):
                out += f"({str(self.__pilha__[i])})" + ", "
                continue
            out += str(self.__pilha__[i]) + ", "
        out = out[:-2] + '|'
        return out

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    p = Pilha()
    print(p.vazia())
    p.empilhar(5)
    p.empilhar(4)
    print(p)
    p.desempilhar()
    print(p)
