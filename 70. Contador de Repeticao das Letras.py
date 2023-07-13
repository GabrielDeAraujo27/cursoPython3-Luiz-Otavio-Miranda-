palavra = str(input('Digite uma frase: ').lower())
print('\n')
c = 0
letrasUsadas = ' ,.:;/°/{}[]ªº=-_+§"!@#$%¨&*()_'
#print(f'\n : {palavra.count(" ")}')
letraMaisUsada = ''
letraMaisUsadaNum = 0
while c < len(palavra): #Um for agilizaria muito esse código
    if palavra[c] not in letrasUsadas:
        print(f'{palavra[c]}: {palavra.count(palavra[c])}')
        letrasUsadas += palavra[c]
        if letraMaisUsadaNum < palavra.count(palavra[c]):
            letraMaisUsada = palavra[c]
            letraMaisUsadaNum = palavra.count(palavra[c])
    c += 1
print(f'A letra mais usada foi {letraMaisUsada} com {letraMaisUsadaNum} usos.')