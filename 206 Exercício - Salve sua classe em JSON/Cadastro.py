import json
from C import pessoa

p1 = pessoa(nome='Gabriel', sobrenome='de Araujo', idade=20, sexo='masculino')
print(p1.__dict__)
p2 = pessoa()
p2.nome = 'Matheus'
p2.sobrenome = 'Oliveira'
p2.idade = 19
p2.sexo = 'masculino'

print(p2.nome)
print(p2.sobrenome)
print(p2.idade)
print(p2.sexo)

with open("class_pessoa.json", "w", encoding="UTF-8") as file:
    json.dump((p1.__dict__, p2.__dict__), file, indent=4)
 #   json.dump(p2.__dict__, file, indent=4)