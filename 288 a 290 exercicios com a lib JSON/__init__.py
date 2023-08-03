import json

def e288():
    with open("string.json", "r", encoding="UTF-8") as arquivo:
        dadosAnteriores = json.load(arquivo)

    string_json = 'string\n' + dadosAnteriores

    #for c in dadosAnteriores:
     #   string_json += c


    with open("string.json", "w", encoding="UTF-8") as arquivo:
        json.dump(string_json, arquivo, indent=4)

    print(string_json)

def f288():


#e288()
v288()