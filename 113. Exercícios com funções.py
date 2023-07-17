import random


def multiplicacao(a, *b):
    print(f'{a}', end=' ')
    for c in b:
        print(f'* {c}', end=' ')
        a = a * c
    return a

def parOuImpar(*a):
    for c in a:
        if c % 2 == 0:
            print(f'{c} é par')
        else:
            print(f'{c} é ímpar')

escolha = str(input('Você deseja multiplicar números(1) ou saber se são pares ou impares(2)? '))
if escolha in '1':
    numMultiplicado = multiplicacao(random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9))
    print(f' = {numMultiplicado}')
elif escolha in '2':
    parOuImpar(random.randint(0,80), random.randint(0,80), random.randint(0,80), random.randint(0,80), random.randint(0,80))