def perguntaEscolha():
    escolha = int(input('\n\n(1)Adicionar tarefa      (2)Desfazer      (3)refazer      (4)Mostrar (9)Encerra\nInsira: '))
    return escolha
def direcionaEscolha(e, listaTarefas):
    global novoItem
    global apagouItem
    if e == 1:
        novoItem = adiciona(listaTarefas)
        return listaTarefas.append(novoItem), novoItem
    elif e == 2:
        desfaz(listaTarefas)
    elif e == 3:
        refaz(listaTarefas)
    else:
        for c in listaTarefas:
            print(c)
        input()
def adiciona(listaTarefas):
    novoItem = str(input('Adicione uma tarefa: '))
    if novoItem in listaTarefas:
        novoItem += ' novamente.'
    return novoItem
def desfaz(listaTarefas):
    global apagouItem
    if novoItem != 0:
        apagouItem = True
        return listaTarefas.remove(novoItem)
def refaz(listaTarefas):
    global apagouItem
    if apagouItem == True:
        apagouItem = False
        return listaTarefas.append(novoItem)
    else:
        print('Não há item para apagar.')