altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))
IMC = peso/(altura*altura)
if altura > 100:
    IMC *= 10000
print(f'IMC: {IMC:.2f}')