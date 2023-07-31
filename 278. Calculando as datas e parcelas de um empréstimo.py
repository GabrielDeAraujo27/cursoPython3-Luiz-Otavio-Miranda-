# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
import datetime
import dateutil.relativedelta

def efetuaEmprestimo():
    emprestimoInicial = valorEmprestimo = 1000
    dataInicial = datetime.datetime.strptime('20/12/2020', '%d/%m/%Y')
    dataFinal = datetime.datetime.strptime('2024-05-02', '%Y-%m-%d')
    numParcela = dataFinal - dataInicial
    numParcela = int(numParcela.days / 31)
    valorEmprestimo = valorEmprestimo + (valorEmprestimo + (numParcela * (0.02 * valorEmprestimo)))
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