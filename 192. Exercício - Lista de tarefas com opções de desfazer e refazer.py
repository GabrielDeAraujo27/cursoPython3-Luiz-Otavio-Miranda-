def PerguntaEscolha():
    escolha = int(input('(1)Adicionar tarefa      (2)Desfazer      (3)refazer      (4)Mostrar (9)Encerra\nInsira: '))
    return escolha
def direcionaEscolha(e):
    global novoItem
    global apagouItem
    if e == 1:
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
    global apagouItem
    if novoItem != 0:
        apagouItem = True
        return listaTarefas.remove(novoItem)
def refaz():
    global apagouItem
    if apagouItem == True:
        apagouItem = False
        return listaTarefas.append(novoItem)
    else:
        print('Não há item para apagar.')


listaTarefas = []
novoItem = int
apagouItem = False

while True:
    escolha = PerguntaEscolha()
    if escolha == 9:
        break
    direcionaEscolha(escolha)
print('Esta é sua lista final\n')
for c in listaTarefas:
    print(c)