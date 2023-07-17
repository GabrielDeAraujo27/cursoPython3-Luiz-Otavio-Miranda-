def multiplicacao(a, *b):
    for c in b:
        d += f'{a} *'
        a = a * c
    return d

numMultiplicado = multiplicacao(1, 2, 8, 5, 4, 6, 7, 2, 9)
print(f' = {numMultiplicado}')