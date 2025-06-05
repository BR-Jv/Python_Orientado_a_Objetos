

class Ponto2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def comparar(self, ponto):
        '''
            Método que faz uma comparação profunda dos pontos2D
        '''
        return  True if self.x == ponto.x and self.y == ponto.y else  False 

    def __add__(self, ponto):
        x = self.x + ponto.x
        y = self.y + ponto.y
        return Ponto2D(x, y)


    def __str__(self):
        return f'x={self.x}, y={self.y}'


