

class Ponto2D:

    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __add__(self, num):
        if type(num) == tuple:
            x = self.x + num[0]
            y = self.y + num[1]
            return (x, y)

        if isinstance(num, Ponto2D):
            x = self.x + num.x
            y = self.y + num.y
            return Ponto2D(x, y)
            

    def __mul__(self, num):
        if type(num) == int:
            return Ponto2D(self.x * num, self.y * num)
        
        if isinstance(num, Ponto2D):
            x = self.x * num.x
            y = self.y * num.y
            return x + y


    def __eq__(self, num):
        if type(num) == tuple:
            
            if num == (self.x, self.y): 
                return True 
            else: 
                return False

        if isinstance(num, Ponto2D):
            
            if self.x == num.x and self.y == num.y : 
                return True 
            else: 
                return False
           
        
    def __getitem__(self, i):
        if i != 0: 
            return self.y

        return self.x


    def __setitem__(self, i, v):
        if i != 0: 
            self.y = v  
        else: 
            self.x = v
    
    
    def __str__(self):
        return f'Ponto2D({self.x},{self.y})'


