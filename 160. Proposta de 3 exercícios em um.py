# copy, sorted, produtos.sort
import copy


def alteraPreco(listaProdutos):
    precoAlterado = copy.deepcopy(listaProdutos)
    for c in precoAlterado:
        c['preco'] = round(c['preco'] * 1.1, 2)
    return precoAlterado

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
novosProdutos = alteraPreco(produtos)
for c in novosProdutos:
    print(c)