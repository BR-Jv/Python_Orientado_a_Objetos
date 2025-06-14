class Relogio():

    def __init__(self, horas, minutos, segundos):
        self._horas = 00
        self._minutos = 00
        self._segundos = 00
        self.set_hora(horas, minutos, segundos)

    def set_hora(self, horas, minutos, segundos):
        """
        Atributo horas deve ser um valor inteiro entre 0 e 23
        Atributo minutos deve ser um valor inteiro entre 0 e 59
        Atributo segundos deve ser um valor inteiro entre 0 e 59
        """        
        if self._validar_hora(horas):
            self._horas = horas 

        if self._validar_minuto(minutos):
            self._minutos = minutos

        if self._validar_segundo(segundos):
            self._segundos = segundos

    def _validar_hora(self, horas):
        if horas >= 0 and horas <= 23:
            return True
        else: 
            return False
    
    def _validar_minuto(self, minutos):
        return self._validar_timer(minutos)
        
    def _validar_segundo(self, segundos):
        return self._validar_timer(segundos)

    def _validar_timer(self, value):
        if value >= 0 and value <= 59:
            return True
        else: 
            return False

    def __str__(self):
        return f"{self._horas:02d}:{self._minutos:02d}:{self._segundos:02d}"

    def marca_segundo(self):
        """
        Avança um segundo no relógio.
        """
        # Virada de minuto: 00:00:59 -> 00:01:00

        if self._segundos != 59:
            self._segundos += 1
        else:
            self._segundos = 00
            self._verifica_minutos()

    def _verifica_minutos(self):
        if self._minutos != 59:
            self._minutos += 1
        else:
            self._minutos = 00
            self._verifica_horas()

    def _verifica_horas(self):
        
        if self._horas != 23:
            self._horas += 1
        else:
            self._horas = 00