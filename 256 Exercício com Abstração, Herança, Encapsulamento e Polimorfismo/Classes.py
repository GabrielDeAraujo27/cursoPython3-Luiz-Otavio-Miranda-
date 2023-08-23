from abc import ABC, abstractmethod

class pessoa(ABC):
    def __init__(self, nomeCompleto=str, idade=int, sexo=str):
        self.nomeCompleto = nomeCompleto
        self.idade = idade
        self.sexo = sexo
class cliente(pessoa):
    ...

class banco(ABC):
    def __init__(self, cliente1 = cliente):
        self.cliente1 = cliente

Marcos = cliente()