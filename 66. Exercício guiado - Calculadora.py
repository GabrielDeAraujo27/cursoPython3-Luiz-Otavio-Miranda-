respT = True
total = float(input('Digite o primeiro número: '))
while respT == True:
    while respT == True:
        try:
            operacao = str(input('Que operação você deseja fazer? '))
            if operacao not in '+-*/':
                raise
        except:
            break
        proximoNúmero = float(input(f'{total} {operacao} '))
        numAnterior = total
        if operacao == '+':
            total += proximoNúmero
        elif operacao == '-':
            total -= proximoNúmero
        elif operacao == '*':
            total *= proximoNúmero
        elif operacao == '/':
            total /= proximoNúmero
        print(f'{numAnterior} {operacao} {proximoNúmero} = {total}')
        respT = bool(input('Deseja continuar? ').lower().startswith('s'))