nome = 'Gabriel'
tamanho = len(nome)
pont = 0
nomeNovo = '*'
while pont < tamanho:
    nomeNovo += f'{nome[pont]}*'
    pont += 1
    #print(nomeNovo)
print(nomeNovo)