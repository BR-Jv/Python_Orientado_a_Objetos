class Gasto:
    '''
    Representa um gasto (despesa)
    de um determinado valor
    com alguma coisa (descrição).
    '''

    def __init__(self, valor, descricao):
        self.valor = valor
        self.descricao = descricao

    def __radd__(self, outro):
        return outro + self.valor

    def __str__(self):
        return f'R${self.valor:.2f} em {self.descricao}'

# Não altere a implementação base fornecida
class CategoriaGastos:
    '''
    Toda gasto será incluso em uma categoria.
    A categoria tem nome e limite de valor.
    '''

    def __init__(self, nome, limite):
        self.nome = nome
        self.limite = limite 
        self._gastos = []
        self._idx = 0 

    def __iter__(self):
        self._idx = 0
        return self

    def __next__(self):
        if self._idx < len(self._gastos):
            x = self._gastos[self._idx]
            self._idx += 1
            return x
        else:
            raise StopIteration

    def adiciona(self, g):
        '''
        Adiciona um gasto g
        à agregação de gastos.
        '''
        self._gastos.append(g)
        # implemente o seu código

    def excede_limite(self):
        '''
        Retorna verdadeiro se a soma
        dos gastos mantidos na agregação
        é maior do que o limite especificado.
        '''
        # implemente o seu código:
        # a função Python sum pode ser utilizada
        # na lista encapsulada por esta classe
        # ou vc pode percorrê-la com for e somar o valor
        # de cada gasto

        if sum(self._gastos) > self.limite:
            return True
        
        return False


class PainelGastos:
    '''
    Um painel de gastos mantém várias categorias
    e informa qual delas excedeu o limite.
    '''

    def __init__(self):
        self.categorias = [
            CategoriaGastos('diarios', 400), 
            CategoriaGastos('extras', 100), 
            CategoriaGastos('medicos', 200)
            ]

    def adiciona_gasto(self, gasto, tipo):
        '''
        Adiciona um gasto a uma
        das categorias, de acordo com
        o parâmetro informando o tipo do gasto.
        '''
        if tipo == 'diarios':
            self.categorias[0].adiciona(gasto)
        if tipo == 'extras':
            self.categorias[1].adiciona(gasto)
        if tipo == 'medicos':
            self.categorias[2].adiciona(gasto)


    def imprime_gastos(self):
        '''
        Imprime os gastos de todas as
        categorias do painel.
        '''
        for categoria in self.categorias:
            print(f'Gasto {categoria.nome}')
            for gasto in categoria._gastos:
                print(gasto)
            print('----------------------')

    def checa_limites(self):
        '''
        Imprime uma mensagem informando
        cada categoria de gastos que
        excedeu o limite.
        '''

        for categoria in self.categorias:
            if categoria.excede_limite():
                print(f'Gastos {categoria.nome} está excedendo o limite de R${categoria.limite}')
