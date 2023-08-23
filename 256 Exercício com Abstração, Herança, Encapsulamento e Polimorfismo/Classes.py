import random
from abc import ABC, abstractmethod

class banco:
    def __init__(self, NomeDaInstituicao):
        self.NomeDaInstituicao = NomeDaInstituicao

class pessoa:
    def __init__(self, nomeCompleto=str, idade=int, sexo=str):
        self.nomeCompleto = nomeCompleto
        self.idade = idade
        self.sexo = sexo
    def cadastraPessoa(self, nome):
        self.nomeCompleto: nome
        self.idade = 18#int(input('Digite sua idade: '))
        self.sexo = 'Masculino'#str(input('Qual o seu sexo: '))
class cliente(pessoa):
    def __init__(self, ContaParticular, pes=pessoa):
        self.nomeCompleto = pes.nomeCompleto
        self.idade = pes.idade
        self.sexo = pes.sexo
        self.MeuBanco = ContaParticular.NomeDaInstituicao
        self.TipoDeConta = ContaParticular.TipoDeConta
        self.NumeroDaConta = ContaParticular.NumeroDaConta
        self.Saldo = ContaParticular.saldo

class conta(ABC):
    @abstractmethod
    def __init__(self, Titular=pessoa, Instituicao=banco):
        self.NomeDoTitular = Titular.nome
        self.NumeroDaConta = random.randint(10000, 99999)
        self.saldo = 0
class contaCorrente(conta):
    def __init__(self, Titular=pessoa, Instituicao=banco):
        self.NomeDoTitular = Titular.nomeCompleto
        self.TipoDeConta = 'Corrente'
        self.NumeroDaConta = random.randint(10000, 99999)
        self.NomeDaInstituicao = Instituicao.NomeDaInstituicao
        self.saldo = 0
class contaPoupanca(conta):
    def __init__(self, Titular=pessoa, Instituicao=banco):
        self.NomeDoTitular = Titular.nome
        self.TipoDeConta = 'Poupanca'
        self.NumeroDaConta = random.randint(10000, 99999)
        self.NomeDaInstituicao = Instituicao.NomeDaInstituicao
        self.saldo = 0

#Bradesco = banco('Bradesco')

