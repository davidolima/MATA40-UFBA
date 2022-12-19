# #########################################
# Define um Tipo Abstrato de Dados (TAD) 
# para armazenar cores no formato RGB
# #########################################

class cCor:

    r = 0.0
    g = 0.0
    b = 0.0

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def setCor(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def setR(self, r):
        self.r = r

    def setG(self, g):
        self.g = g

    def setB(self, b):
        self.b = b

    def getCor(self):
        return self.r, self.g, self.b

    def getR(self):
        return self.r

    def getG(self):
        return self.g

    def getB(self):
        return self.b

    def __str__(self):
        return f'[ {self.r} , {self.g} , {self.b} ]'

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            r = self.r * other
            g = self.g * other
            b = self.b * other

        if isinstance(other, cCor):
            r = self.r * other.r
            g = self.g * other.g
            b = self.b * other.b

        return self.__class__(r, g, b)
