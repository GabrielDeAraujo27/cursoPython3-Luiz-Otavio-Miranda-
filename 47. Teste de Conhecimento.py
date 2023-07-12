nome = str(input('Qual é o seu nome? '))
#idade = int(input('Qual a sua idade? '))

if nome == '':
    print('Você não preencheu todos os campos')
else:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}.')
    print(f'Seu nome contém {nome.count(" ")} espaços.')
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[len(nome)-1]}')