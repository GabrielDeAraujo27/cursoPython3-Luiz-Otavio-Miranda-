def uneCidadeEstado(x, y):
    for c in range(0, min(len(x), len(y))):
        print(x[c], y[c], sep=' - ')

listaDeCidades = ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Rio de Janeiro', 'Goiania']
listaDeEstados = ['BA', 'SP', 'MG', 'RJ']
uneCidadeEstado(listaDeCidades, listaDeEstados)