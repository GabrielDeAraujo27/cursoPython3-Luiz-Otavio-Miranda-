import random

CPF = []
for primeiroNumero in range (0, 9):
   CPF.append(random.randint(0,9))
multiplicador = 10
primeiroNumero = 0
for c in CPF:
    primeiroNumero += c * multiplicador
    multiplicador -= 1
primeiroNumero *= 10
primeiroNumero %= 11
primeiroNumero = 0 if primeiroNumero > 9 else primeiroNumero
CPF.append(primeiroNumero)

multiplicador = 11
segundoNumero = 0
for c in CPF:
    segundoNumero += c * multiplicador
    multiplicador -= 1
segundoNumero *= 10
segundoNumero %= 11
segundoNumero = 0 if segundoNumero > 9 else segundoNumero

CPF.append(segundoNumero)
#print(primeiroNumero, segundoNumero)

for c in CPF:
    print(c, end='')