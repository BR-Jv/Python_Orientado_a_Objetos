
class Robo:
    def __init__(self, nome, posicao):
        self.__nome = nome
        self.__posicao = posicao
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if type(nome) == str:
            self.__nome = nome
        else: 
            print('Erro: nome do robô deve ser uma string')
    
    @property
    def pos(self):
        return self.__posicao


    def __str__(self):
        return f'{self.__nome} em ({self.__posicao[0]},{self.__posicao[1]})'

    def move(self, dx, dy):
        self.__posicao[0] += dx
        self.__posicao[1] += dy

class Setor: 

    def __init__(self, codigo, coordenadas):
        self.codigo = codigo
        self.__posto_sd = coordenadas[0] #superior/direita
        self.__posto_ie = coordenadas[1] # inferior/esquerda
        self.robos = [] #robôs opernado no setor

    def esta_dentro(self, robo):
        if self.__posto_ie[0] <= robo.pos[0] <= self.__posto_sd[0]:
            if self.__posto_ie[1] <= robo.pos[1] <= self.__posto_sd[1]:
                return True
            
        return False
    
    def adiciona(self, robo):
        if self.esta_dentro(robo):
            self.robos.append(robo)
            return True
        
        return False
    

    def imprime(self):
        print(f'Robôs operando dentro do setor {self.codigo}.')
        for robo in self.robos: 
            print(robo)

class Armazem:

    def __init__(self):
        self.__setores = [
            Setor('1001', [(10, 10), (0, 0)]),
            Setor('1002', [(0, 10), (-10, 0)]),
            Setor('1003', [(10, 0), (0, -10)]),
        ]
        self.__setoresNull = []

    def adiciona_robo(self, robo):
        
        for setores in self.__setores:
            if setores.adiciona(robo):
                print(f'{robo.nome} adicionado ao setor {setores.codigo}')
                StopIteration
                return 0
            
        self.__setoresNull.append(robo)

    def imprime_robos(self):
        print('Robôs do armazem')
        for setores in self.__setores:
            setores.imprime()
        
        print('Robôs não alocados')
        for robos in self.__setoresNull:
            print(robos)
            
    