from Classes import pessoa, cliente, contaCorrente, contaPoupanca, banco

def consulta(MCliente=cliente):
    print(f'Nome do usuario: {MCliente.nomeCompleto}\n'
          f'Banco: {MCliente.MConta.NomeDaInstituicao}\n'
          f'Numero da conta: {MCliente.MConta.NumeroDaConta}\n'
          f'Tipo de conta: {MCliente.MConta.TipoDeConta}\n'
          f'Saldo: {MCliente.MConta.saldo}')
def criaConta():
    pessoa1 = pessoa(nomeCompleto='Gabriel')  # pessoa(nomeCompleto=input('Digite seu nome: '))
    pessoa1.cadastraPessoa(pessoa)
    print(pessoa1.__dict__)
    meuBanco = Bradesco
    minhaConta = contaCorrente(pessoa1, meuBanco)
    cliente1 = cliente(minhaConta, pessoa1)
    return cliente1