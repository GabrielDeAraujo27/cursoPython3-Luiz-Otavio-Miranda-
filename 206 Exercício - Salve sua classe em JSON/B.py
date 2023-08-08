import json
from C import pessoa

with open("class_pessoa.json", "r", encoding="UTF-8") as p:
    pe2 = json.load(p)
    p = []
    for c in range(len(pe2)):
        p.append(pessoa(nome=pe2[c]['nome'], sobrenome=pe2[c]['sobrenome'], sexo=pe2[c]['sexo'], idade=pe2[c]['idade']))

for c in p:
    print('Nome: ', c.nome, c.sobrenome)
    print('sexo: ', c.sexo)
    print('idade: ', c.idade, '\n')