compras = []
while True:
    opcao = input('(i)nserir         (a)pagar          (l)istar\n')
    if opcao in 'Ii1':
        compras.append(input('Que produto você deseja adicionar? '))
    elif opcao in 'Aa':
        try:
            compras.pop(int(input('Que produto você deseja remover? ')))
        except:
            print('valor inválido')
    elif opcao in 'Ll':
        for c in compras:
            print((compras.index(c)), c)