def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def executa(funcao, x):
    def funcaoInterna(y):
        return funcao(x, y)
    return funcaoInterna


somaCom5 = executa(soma, 5)
multiplicaPor10 = executa(multiplica, 10)

print(somaCom5(5))
print(multiplicaPor10(10))