def direcionaEscolha(e):
    if e == 1:
        novoItem = adiciona()
        return novoItem
    elif e == 2:
        desfaz()
    elif e == 3:
        refaz()
    else:
        for c in listaTarefas:
            print(c)
def adiciona(e):
    novoItem = str(input('Adicione uma tarefa: '))
    if novoItem is in listaTarefas:
        novoItem += ' novamente.'

    return novoItem


listaTarefas = ['']

escolha = input('(1)Adicionar tarefa      (2)Desfazer      (3)refazer      (4)Mostrar'
                '\nInsira: ')

direcionaEscolha(e)