palavraSecreta = 'python'
for b in range(4,0,-1):
    palpite = str(input('Qual o seu palpite? ').lower())
    if palpite == palavraSecreta:
        print('Parabéns, você acertou!')
        quit()
    for c in range(0,len(palpite)):
        if palpite[c] in palavraSecreta:
            print(f'Você acertou a letra {palpite[c]}')
    if b>1:
        print(f'Você ainda tem {b-1} tentativas')
print('Infelizmente você perdeu.')
