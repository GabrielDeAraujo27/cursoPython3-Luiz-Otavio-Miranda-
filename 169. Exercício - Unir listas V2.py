listaDeCidades = ('Salvador', 'Ubatuba', 'Belo Horizonte', 'Rio de Janeiro', 'Goiania')
listaDeEstados = ('BA', 'SP', 'MG', 'RJ', 'GO', 'SP')
cidadeEstado = zip(listaDeCidades, listaDeEstados)

for c in cidadeEstado:
    print(c)