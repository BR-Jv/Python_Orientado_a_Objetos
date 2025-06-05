class CartaoTransporte:

    def __init__(self):
        self.__codigo = 0
        self.__viagens = 0
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def viagens(self):
        return self.__viagens

    @codigo.setter
    def codigo(self, codigo):
        if type(codigo) != int:
            print("O código precisa ser um nr. inteiro")
            # raise Exception("Valor invalido para código")
            return 0
        
        self.__codigo = codigo


    def __str__(self):
        return f"Código:{self.__codigo}, viagens:{self.__viagens}"


    def carrega(self, viagens):
        if viagens <= 0:
            # raise Exception("Informe um valor maior que zero.")
            print("Carregamento inválido: nr. de viagens precisa ser maior que 0")
            return 0
        
        self.__viagens = viagens
        print(f"Carregamento confirmado. Viagens: {self.__viagens}")


    def usa(self):
        if self.__viagens <= 0:
            # raise Exception(f"Seu saldo é de: {self.__viagens}")
            print(f"Cartão sem viagens disponíveis.")
            return 0
        
        self.__viagens = self.__viagens - 1    
        print(f"Boa viagem. Viagens: {self.__viagens}")




# Para teste. Colocar na função main 
# c1 = CartaoTransporte()
    
#     c1.codigo = 23.5
#     print(c1)
#     c1.codigo = 1553
#     print(c1)

#     c1.carrega(-5)
#     c1.carrega(3)
#     print(c1)

#     c1.usa()
#     c1.usa()
#     c1.usa()
#     c1.usa()

#     c1.carrega(5)
#     print(f'Dados do cartão - Código: {c1.codigo}, viagens: {c1.viagens}')