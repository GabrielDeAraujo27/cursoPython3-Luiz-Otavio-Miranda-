from func195 import  direcionaEscolha, perguntaEscolha
import json

try:
    with open("Lista_de_Tarefas.json", "r", encoding="UTF-8") as arquivo:
        dadosAnteriores = json.load(arquivo)
except (json.decoder.JSONDecodeError, FileNotFoundError):
    dadosAnteriores = ''


listaTarefas = ['Terminar esse modulo', 'dormir', 'comecar o proximo modulo']
for c in dadosAnteriores:
    listaTarefas.append(c)
novoItem = int
apagouItem = False


while True:
    escolha = perguntaEscolha()
    if escolha == 9:
        break
    direcionaEscolha(escolha, listaTarefas)

print('\nAlteração completa')
#for c in listaTarefas:
 #   print(c)

with open("Lista_de_Tarefas.json", "w", encoding="UTF-8") as arquivo:
    json.dump(listaTarefas, arquivo, indent=4)