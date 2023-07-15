import random

CPF = []
for a in range (0,9):
   CPF.append(random.randint(0,9))
b = 10
a = 0
for c in CPF:
    a += c * b
    b -= 1
a *= 10
a %= 11
a = 0 if a>9 else a
CPF.append(a)

b = 11
aa = 0
for c in CPF:
    aa += c * b
    b -= 1
aa *= 10
aa %= 11
aa = 0 if aa>9 else aa

CPF.append(aa)
print(a, aa)

for c in CPF:
    print(c, end='')