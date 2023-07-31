import datetime
import dateutil.relativedelta

def efetuaEmprestimo():
    while True:
        try:
            emprestimoInicial = valorEmprestimo = float(input(f'Qual o valor que você deseja? '))
            numParcela = int(input(f'Você deseja pagar em quantas parcelas? '))
        except ValueError:
            print('O valor inserido é inválido')
        else:
            break

    dataInicial = datetime.datetime.now()
    valorEmprestimo = valorEmprestimo + (valorEmprestimo + (numParcela * (0.08 * valorEmprestimo)))
    valorParcela = round(valorEmprestimo / numParcela, 2)
    print(valorParcela)
    emprestimo(emprestimoInicial, valorEmprestimo, dataInicial, valorParcela, numParcela)

def emprestimo(inicial, emprestimo, dataAtual, parcela, numParcela):
    diferenca = 0
    for c in range(0, numParcela):
        dataAtual += dateutil.relativedelta.relativedelta(months=1)
        data = datetime.datetime.strftime(dataAtual, '%d/%m/%Y')

        print(f'\n\nData: {data[0:10]}')
        print(f'Dívida restante: {round(emprestimo, 2)}')

        if (emprestimo - parcela)>0:
            emprestimo -= parcela
            if emprestimo<parcela:
                parcela += emprestimo
                emprestimo = 0
        else:
            diferenca = parcela - emprestimo
            emprestimo = 0


        print(f'Valor da parcela: {round((parcela-diferenca),2)}')
        print(f'Dívida após o pagamento: {round(emprestimo, 2)}')
        if emprestimo == 0:
            print(f'\nDivida de {inicial} quitada')


efetuaEmprestimo()