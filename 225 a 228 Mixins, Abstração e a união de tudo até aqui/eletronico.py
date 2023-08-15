from logy import logPrintMixin
from abc import ABC, ABCMeta, abstractmethod

class eletronico(ABC):
    def __init__(self, nome):
        self.nome = nome
        self._ligado = False

    @abstractmethod
    def ligar(self):
        if not self._ligado:
            self._ligado = True

    @abstractmethod
    def desligar(self):
        if self._ligado:
            self._ligado = False

class smartPhone(eletronico, logPrintMixin):
    def ligar(self):
        if self._ligado == False:
            super().ligar()
            self.log_success(f'{self.nome} está ligado')
        else:
            self.log_error(f'{self.nome} está desligado')

    def desligar(self):
        super().desligar()
        if self._ligado:
            super().ligar()
            self.log_success(f'{self.nome} está desligado')
        else:
            self.log_error(f'{self.nome} está ligado')