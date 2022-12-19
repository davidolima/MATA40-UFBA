class No:
    def __init__(self, valor=None):
        self.__valor__ = valor
        self.__prox__ = None

    def __str__(self): return str(self.__valor__)

    def setValor(self, valor): self.__valor__ = valor 

    def setProx(self, prox): self.__prox__ = prox

    def getValor(self): return self.__valor__

    def getProx(self): return self.__prox__


class ListaEnc:
    def __init__(self, *elementos):
        self.__inicio__     = None
        self.__tamanho__   = 0
        self.__indice__ = 0

        for elemento in elementos:
            self.inserir(elemento)

    def __str__(self):
        outStr = "<"
        if self.__tamanho__ != 0:
            x = self.__inicio__
            while x.getProx() != None:
                outStr += str(x.getValor()) + ", "
                x = x.getProx()
            outStr += str(x.getValor())
                
        outStr += ">"
        return outStr
    
    def __repr__(self): return self.__str__()

    def __getitem__(self, n): # lEnc[n] -> valor
        try:
            n = int(n)
        except:
            raise TypeError("ERROR: Índice deve ser um inteiro.")

        if self.__tamanho__ == 0 or n > self.__tamanho__ or n < 0:
            return -1

        x = self.__inicio__
        indice = 0
        while (x != None):
            if (indice == n):
                return x.getValor()

            x = x.getProx()
            indice += 1
    
    def __setitem__(self, n, valor): # lEnc[n] = valor 
        if self.__tamanho__ == 0 or n > self.__tamanho__ or n < 0:
            return

        x = self.__inicio__
        while(x.getProx() != None):
            x = x.getProx()

        x.setDado(valor)

    def __iter__(self) -> int:
        self.__indice__ = 0
        return self

    def __next__(self) -> int:
        if(self.__indice__ >= self.__tamanho__):
            raise StopIteration

        x = self.__getitem__(self.__indice__)
        self.__indice__ += 1
        return x
    
    def __add__(self,other):
        if isinstance(other, ListaEnc) or isinstance(other, list):
            for i in other:
                self.inserir(i)
            return self

    def __len__(self) -> int: return self.__tamanho__
    def tamanho(self) -> int: return self.__tamanho__

    def inserir(self, n):
        novo = No(n)

        if self.__tamanho__ == 0:
            self.__inicio__ = novo
            self.__tamanho__ += 1
            return

        x = self.__inicio__
        while(x.getProx() != None):
            x = x.getProx()

        self.__tamanho__ += 1
        x.setProx(novo)


    def remover(self, n) -> bool:
        if self.__tamanho__ == 0:
            return

        if self.__inicio__.getValor() == n:
            self.__inicio__ = self.__inicio__.getProx()
            self.__tamanho__ -= 1
            return

        x = self.__inicio__
        while (x.getProx() != None and x.getProx().getValor() != n):
            x = x.getProx()

        if (x.getProx() == None):
            return

        self.__tamanho__ -= 1
        x.setProx(x.getProx().getProx())
        return
    
    def esvaziar(self):
        self.__inicio__ = None
        self.__tamanho__ = 0