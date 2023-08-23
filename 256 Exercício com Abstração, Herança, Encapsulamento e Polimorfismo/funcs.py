from Classes import pessoa, cliente, contaCorrente, contaPoupanca, banco

Bradesco = banco('Bradesco')
def consulta(MCliente=cliente):
    print(f'Nome do usuario: {MCliente.nomeCompleto}\n'
          f'Banco: {MCliente.MConta.NomeDaInstituicao}\n'
          f'Numero da conta: {MCliente.MConta.NumeroDaConta}\n'
          f'Tipo de conta: {MCliente.MConta.TipoDeConta}\n'
          f'Saldo: {MCliente.MConta.saldo}')
def criaConta():
    pessoa1 = pessoa(nomeCompleto=input('Digite seu nome: '))
    pessoa1.cadastraPessoa(pessoa)
    print(pessoa1.__dict__)
    meuBanco = Bradesco
    escolha = int(input('(1)Conta Corrente\n(2)Conta Poupança\n'))
    try:
        if escolha == 1:
            minhaConta = contaCorrente(pessoa1, meuBanco)
        elif escolha == 2:
            minhaConta = contaPoupanca(pessoa1, meuBanco)
        else:
            raise TypeError
    except TypeError:
        print('Valor inválido')
    cliente1 = cliente(minhaConta, pessoa1)
    return cliente1
def menu(cliente1):
    while True:
        escolha = input('(1)Consulta\n(2)Saque\n(3)Deposito\n')
        if escolha == '1':
            consulta(cliente1)
        elif escolha == '2':
            cliente1.MConta.Saque()
        elif escolha == '3':
            cliente1.MConta.Deposito()
        else:
            print('Valor inválido')
            break
        input()