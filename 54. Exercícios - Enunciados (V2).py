from time import strftime

def analisePar():
    try:
        num = int(input('Digite um número: '))
    except:
        print('Este não é um número inteiro.')
    else:
        if num % 2 == 0:
            print(f'{num} é um número par.')
        else:
            print(f'{num} é um número ímpar.')
def saudaçãoAdequada(nome):
    try:
        hora = float(strftime("%H.%M"))
    except:
        print('Horário invalido')
    else:
        if hora < 12:
            print(f'Bom dia, {nome}.')
        elif hora > 18:
            print(f'Boa noite, {nome}.')
        else:
            print(f'Boa tarde, {nome}.')
def nomeCurto(nome):
    if len(nome) <= 4:
        print('Seu nome é curto!')
    else:
        print('Seu nome é normal.')


nome = str(input('Qual é o seu nome? '))
try:
    print(f'(1)Verifique se um número é par. \n'
          f'(2)Receba uma saudação apropriada.\n'
          f'(3)Saiba se seu nome é curto.')
    escolha = str(input('O que você deseja: '))
    if escolha not in ('1234'):
        raise
except:
    print('Valor invalido')
else:
    if escolha == '1':  # (1)Verifique se um número é par.
        analisePar()
    elif escolha == '2':  # f'(2)Receba uma saudação apropriada.
        saudaçãoAdequada(nome)
    elif escolha == '3':  # (3)Saiba se seu nome é curto.
        nomeCurto(nome)
finally:
    print('...\nProcesso encerrado.\n...')