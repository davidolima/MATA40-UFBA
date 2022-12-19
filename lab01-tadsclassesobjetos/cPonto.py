# #########################################
# Define um Tipo Abstrato de Dados (TAD) 
# para armazenar pontos em 2D
# #########################################

class cPonto:

    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print(f'Pto =  ( {self.x} , {self.y} )')

    def __str__(self):
        return f'( {self.x} , {self.y } )'

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            x = self.x + other
            y = self.y + other

        return self.__class__(x, y)
