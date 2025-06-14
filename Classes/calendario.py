class Calendario():

    ultimo_dia_mes = (31,28,31,30,31,30,31,31,30,31,30,31)

    @staticmethod
    def ehBissexto(ano):
        """ 
        O metodo retorna True se o parametro ano é ano bissexto, False caso contrario
        """
        # para ser ano bissexto:
        #     é ano % 4 == 0
        # nao é ano % 100 == 0
        # nao é ano % 400 == 0
        if (ano%4==0 and ano%100!=0) or (ano%400==0):
            return True
        else:
            return False 

    def __init__(self, dia, mes, ano):
        self.__dias = 0
        self.__meses = 0
        self.__anos = 0
        self.set_data(dia, mes, ano)

    def set_data(self, dia, mes, ano):
        """
        dia, mes e ano devem ser numeros inteiros
        """
        if self._verifica_data(dia):
            self.__dias = dia

        if self._verifica_data(mes):
            self.__meses = mes

        if self._verifica_data(ano):
            self.__anos = ano

    def _verifica_data(self, data):
        if type(data) == int:
            return True
        else:
            return False

    def __str__(self):
        return "{0:02d}/{1:02d}/{2:4d}".format(self.__dias,
                                               self.__meses,
                                               self.__anos)
    
    def avanca_dia(self):
        """
        Avança um dia no calendário.
        """       

        if self.__dias in self.ultimo_dia_mes:
            if self.ehBissexto(self.__anos) and self.__meses == 2:
                self.__dias += 1 
            else:
                self._avancar_mes()
        else : 
            self.__dias += 1 

    def _avancar_mes(self):
        if self.__meses == 12: 
            self._avancar_ano()
        else: 
            self.__meses += 1 
            self.__dias = 1
    
    def _avancar_ano(self):
        self.__anos += 1 
        self.__meses = 1
        self.__dias = 1
