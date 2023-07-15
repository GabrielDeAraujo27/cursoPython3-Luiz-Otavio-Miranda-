"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
CPF = '746.824.890'
novoCPF = []

#transforma em int
for c in CPF:
    if c.isnumeric():
        novoCPF.append(int(c))
print(novoCPF)

#multiplica cada número
b = 10
for c in range(0, len(novoCPF)):
    novoCPF[c] = novoCPF[c] * b
    print(b, end='.')
    b -= 1
print('\n', novoCPF, sep='')

#soma todos os números + multiplica por 10 + resto por 11
opCPF = (sum(novoCPF) * 10) % 11
print(opCPF)

#define o primeiro digito
primeiroDigitoCPF = 0 if opCPF>9 else opCPF
print(primeiroDigitoCPF)