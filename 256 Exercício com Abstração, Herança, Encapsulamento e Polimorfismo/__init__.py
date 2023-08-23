from Classes import pessoa, cliente, conta, contaCorrente, contaPoupanca, banco

Bradesco = banco('Bradesco')

pessoa1 = pessoa(nomeCompleto='Gabriel')#pessoa(nomeCompleto=input('Digite seu nome: '))
pessoa1.cadastraPessoa(pessoa)
print(pessoa1.__dict__)
meuBanco = Bradesco
minhaConta = contaCorrente(pessoa1, meuBanco)
cliente1 = cliente(minhaConta, pessoa1)

#Criar uma forma de consultar os dados
#Criar def de saque e deposito
#Criar função que armazena contas