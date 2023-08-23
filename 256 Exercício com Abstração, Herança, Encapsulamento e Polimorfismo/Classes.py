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
        self.MConta = ContaParticular

class conta(ABC):
    @abstractmethod
    def __init__(self, Titular=pessoa, Instituicao=banco):
        self.NomeDoTitular = Titular.nome
        self.NumeroDaConta = random.randint(10000, 99999)
        self.saldo = 0
    @abstractmethod
    def Saque(self):
        while True:
            valorSaque = float(input('Quanto você quer sacar? '))
            if valorSaque <= 0:
                break
            elif (self.saldo - valorSaque) < 0:
                print('Transação invalida')
            else:
                self.saldo -= valorSaque
    def Deposito(self):
        while True:
            valorDeposito = float(input('Quanto você quer depositar? '))
            if valorDeposito <= 0:
                break
            else:
                self.saldo += valorDeposito
                break

class contaCorrente(conta):
    def __init__(self, Titular=pessoa, Instituicao=banco):
        self.NomeDoTitular = Titular.nomeCompleto
        self.TipoDeConta = 'Corrente'
        self.NumeroDaConta = 10#random.randint(10000, 99999)
        self.NomeDaInstituicao = Instituicao.NomeDaInstituicao
        self.saldo = 1000
    def Saque(self):
        while True:
            valorSaque = float(input('Quanto você quer sacar? '))
            if valorSaque <= 0:
                break
            elif (self.saldo - valorSaque) < -500:
                print('Transação invalida')
            else:
                self.saldo -= valorSaque
                break

class contaPoupanca(conta):
    def __init__(self, Titular=pessoa, Instituicao=banco):
        self.NomeDoTitular = Titular.nome
        self.TipoDeConta = 'Poupanca'
        self.NumeroDaConta = 10#random.randint(10000, 99999)
        self.NomeDaInstituicao = Instituicao.NomeDaInstituicao
        self.saldo = 0
    def Saque(self):
        while True:
            valorSaque = float(input('Quanto você quer sacar? '))
            if valorSaque <= 0:
                break
            elif (self.saldo - valorSaque) < 0:
                print('Transação invalida')
            else:
                self.saldo -= valorSaque