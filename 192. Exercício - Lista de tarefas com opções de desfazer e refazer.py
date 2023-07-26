def direcionaEscolha(e):
    if e == 1:
        global novoItem
        novoItem = adiciona()
        return listaTarefas.append(novoItem), novoItem
    elif e == 2:
        desfaz()
    elif e == 3:
        refaz()
    else:
        for c in listaTarefas:
            print(c)
def adiciona():
    novoItem = str(input('Adicione uma tarefa: '))
    if novoItem in listaTarefas:
        novoItem += ' novamente.'
    return novoItem
def desfaz():
    indiceItemApagado = listaTarefas.index(novoItem)
    return listaTarefas.remove(novoItem)


listaTarefas = []
novoItem = 0

while True:
    escolha = int(input('(1)Adicionar tarefa      (2)Desfazer      (3)refazer      (4)Mostrar'
                    '\nInsira: '))

    direcionaEscolha(escolha)