nome = 'Gabriel'
sobrenome = 'de Araújo'
idade = 20
ano_Nascimento = 2023 - idade
maior_de_Idade = str(idade >= 18)
altura_Metros = 1.81
if maior_de_Idade == 'True':
    maior_de_Idade = 'Sim'
else:
    maior_de_Idade = 'Não'

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Nome completo:', nome, sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_Nascimento)
print('É maior de idade?', maior_de_Idade)
print('Altura em metros:', altura_Metros)