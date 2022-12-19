# #########################################
# Define um Tipo Abstrato de Dados (TAD) 
# para armazenar pontos em 2D com cor
# #########################################

import cCor

class cPontoCor:

    x = 0.0
    y = 0.0
    cor = cCor.cCor(0, 0, 0)

    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.cor = c

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getCorPto(self):
        return self.cor

    def print(self):
        print("Pto =  ")
        print(f'( {self.x} , {self.y} ) {self.cor}')

    def __str__(self):
        return f'( {self.x} , {self.y } ) {self.cor}'

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            x = self.x + other
            y = self.y + other

        if isinstance(other, cPonto):
            x = self.x + other.x
            y = self.y + other.y
            c = self.cor + other.cor

        return self.__class__(x, y, c)
