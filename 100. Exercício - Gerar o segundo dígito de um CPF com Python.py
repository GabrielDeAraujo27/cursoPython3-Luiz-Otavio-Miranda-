import copy

CPF = '746.824.890'
novoCPF = []
#transforma em int
for c in CPF:
    if c.isnumeric():
        novoCPF.append(int(c))
print(novoCPF)

#multiplica cada número
b = len(novoCPF)+1
novoCPFp = copy.copy(novoCPF)
for c in range(0, len(novoCPF)):
    novoCPFp[c] = novoCPF[c] * b
    print(b, end='.')
    b -= 1
print('\n', novoCPFp, sep='')

#soma todos os números + multiplica por 10 + resto por 11
opCPF = (sum(novoCPFp) * 10) % 11
print(opCPF)

#define o primeiro digito
primeiroDigitoCPF = 0 if opCPF>9 else opCPF
print(primeiroDigitoCPF)

###############################################
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
novoCPF.append(primeiroDigitoCPF)

#multiplica cada número
b = len(novoCPF)+2
novoCPFp = copy.copy(novoCPF)
for c in range(0, len(novoCPF)):
    novoCPFp[c] = novoCPF[c] * b
    print(b, end='.')
    b -= 1
print('\n', novoCPFp, sep='')

#soma todos os números + multiplica por 10 + resto por 11
opCPF = (sum(novoCPFp) * 10) % 11
print(opCPF)

#define o primeiro digito
primeiroDigitoCPF = 0 if opCPF>9 else opCPF
print(primeiroDigitoCPF)