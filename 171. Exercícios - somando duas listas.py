lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
for c in range(0, min(len(lista_a), len(lista_b))):
    print(lista_a[c]+lista_b[c])