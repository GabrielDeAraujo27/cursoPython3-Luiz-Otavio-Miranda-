firstNum = int(input('Digite o primeiro número: '))
secondNum = int(input('Digite o segundo número: '))

if firstNum>secondNum:
    print(f'{firstNum} é o maior número.')
elif firstNum<secondNum:
    print(f'{secondNum} é o maior número')
else:
    print('Os números são iguais')