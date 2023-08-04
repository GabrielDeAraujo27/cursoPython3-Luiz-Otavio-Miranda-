#random gera números pseudoaleatorios
import random

#random.seed(0)
print(random.randrange(0, 100, 5))
print(random.randint(1,100))
print(random.uniform(5, 15))
lista = [1,2,3,4,5,6,7,8,9]
random.shuffle(lista)
print(lista)
print(random.sample(lista, k=2))
novaLista = random.sample(lista, k=len(lista))
print(novaLista)
print(random.choices(lista, k=10))


#secrets gera números realmente aleatórios
import secrets
print(secrets.choice(lista))
print(secrets.randbelow(999))



random.seed(secrets.randbelow(100))
print(random.randrange(0, 100, 5))
print(random.randint(1,100))
print(random.uniform(5, 15))