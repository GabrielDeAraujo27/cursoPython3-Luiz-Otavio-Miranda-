try:
    print(f'(1)Verifique se um número é par. \n'
          f'(2)Receba uma saudação apropriada.\n'
          f'(3)Saiba se seu nome é curto.')
    esc = str(input('O que você deseja: '))
    if esc not in ('1234'):
        raise
except:
    print('Valor invalido')
else:
    if esc == '1':                         #(1)Verifique se um número é par.
        try:
            num = int(input('Digite um número: '))
        except:
            print('Este não é um número inteiro.')
        else:
            if num % 2 == 0:
                print(f'{num} é um número par.')
            else:
                print(f'{num} é um número ímpar.')
    elif esc == '2':                        #f'(2)Receba uma saudação apropriada.
        try:
            hora = float(input('Que hora são: '))
            if hora>24 or hora<0:
                raise
        except:
            print('Horário invalido')
        else:
            if hora < 12:
                print('Bom dia.')
            elif hora > 18:
                print('Boa noite.')
            else:
                print('Boa tarde.')
    elif esc == '3':                        #(3)Saiba se seu nome é curto.
        try:
            nome = str(input('Qual é o seu nome? '))
        except:
            print('Nome inválido.')
        else:
            if len(nome) <= 4:
                print('Seu nome é curto!')
            else:
                print('Seu nome é normal.')
finally:
    print('...\nProcesso encerrado.\n...')
