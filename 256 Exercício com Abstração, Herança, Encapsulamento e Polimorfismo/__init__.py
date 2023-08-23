from Classes import pessoa, cliente, contaCorrente, contaPoupanca, banco
from funcs import consulta, criaConta



Bradesco = banco('Bradesco')

escolha = 1#int(input('(1)Criar conta'))

if escolha == 1:
    cliente1 = criaConta()

#consulta(cliente1)
cliente1.MConta.Saque()
cliente1.MConta.Deposito()
consulta(cliente1)

#Criar função que armazena contas