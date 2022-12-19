class No:
    def __init__(self, dado=None):
        self.__dado__ = dado
        self.__prox__ = None

    def __del__(self):
        print(f'Apagando {self.__dado__}')
        del self

    def __str__(self):
        return str(self.__dado__)

    def setDado(self, dado):
        self.__dado__ = dado

    def setProx(self, prox):
        self.__prox__ = prox

    def getDado(self):
        return self.__dado__

    def getProx(self):
        return self.__prox__ 
