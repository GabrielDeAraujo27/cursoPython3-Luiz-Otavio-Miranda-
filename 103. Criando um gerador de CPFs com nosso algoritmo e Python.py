import random

CPF = []
CPFp = []
CPFl = []
for a in range (0,9):
    CPF.append(random.randint(0,9))
b = 10
for c in range(0, 9):
    CPFp.append(CPF[c] * b)
    a = sum(CPFp)
    a = a * 10
    a = a % 11
    CPFl.append(a)
    b -= 1
    CPFp.clear()
print(CPF)
print(CPFl)