def verificadorDeResposta (nome, numQuestao, questao):
    print(questao["Pergunta"])
    for b in questao["Alternativas"]:
        print(b)
    resposta = str(input(f'Qual a sua resposta? '))
    if resposta == questao["Resposta"][1]:
        print(f'Acertou!')
        return 1
    else:
        print(f'Errou, a questão certa era {questao["Resposta"]}')
        return 0

perguntas = [
    {
        "Pergunta": "Qual o idioma oficial do Brasil? ",
        "Alternativas": ["(1). Brasileiro", "(2). Inglês", "(3). Português", "(4). Espanhol"],
        "Resposta": "(3). Português"},
    {
        "Pergunta": "Quem foi o inventor responsável pela criação do avião? ",
        "Alternativas": ["(1). Santos Dumont", "(2). Irmãos Wright", "(3). Phoenix Wright", "(4). Taz Mania"],
        "Resposta": "(1). Santos Dumont"
    },
    {
        "Pergunta": "Qual o nome do melhor boss do popular jogo Dark Souls? ",
        "Alternativas": ["(1). Gwyn", "(2). Nito", "(3). Artorias", "(4). Asylum Demon"],
        "Resposta": "(3). Artorias"
    }
]
print('Bem vindo ao Quiz!')
nome = 'Gabriel'#input('Qual é o seu nome? ')
print(f'Certo, {nome}, vamos começar.')
score = 0
for c in range(0, 3):
    score += verificadorDeResposta(nome, c, perguntas[c])
    print(f'{nome}: {score}')
