def analisaLista(cidades, estados):
    if len(cidades)==len(estados):
        uneCidadeEstado(cidades, estados)
    elif len(cidades)>len(estados):
        cidadesAdaptado = []
        for c in range(0, len(estados)):
            cidadesAdaptado.append(cidades[c])
        uneCidadeEstado(cidadesAdaptado, estados)
    else:
        estadosAdaptado = []
        for c in range(0, len(cidades)):
            estadosAdaptado.append(estados[c])
        uneCidadeEstado(cidades, estadosAdaptado)

def uneCidadeEstado(x, y):
    for c in range(0, len(y)):
        print(x[c], y[c], sep=' - ')

listaDeCidades = ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Rio de Janeiro', 'Goiania']
listaDeEstados = ['BA', 'SP', 'MG', 'RJ']
analisaLista(listaDeCidades, listaDeEstados)

'Futuramente será alterado...'