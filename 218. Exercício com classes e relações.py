class marca:
    def __init__(self, nomeMarca=''):
        self.nomeMarca = nomeMarca

    def defineMarca(self):
        self.nomeMarca = 'Honda' #input('Qual o nome da marca? ')
        return self

class motor:
    def __init__(self, nomeMoto=''):
        self.nomeMoto = nomeMoto

class carro:
    def __init__(self, modelo='', marcab='', motorb=''):
        self.modelo = modelo
        self.marcab = marcab
        self.motorb = motorb

    def defineCarro(self, modelo='', marcab='', motorb=''):
        self.modelo = modelo #input('Qual a nome desse carro? ')
        self.motorb = motorb
        self.marcab = marcab
        return self

fiat = marca('Fiat')
motor900b = motor('Motor 900b')
volkswagen = marca('Volkswagen')

meuCarro = carro
meuCarro.defineCarro(meuCarro, 'Sedan', fiat, motor900b)

seuCarro = carro('Sport')
seuCarro.motorb = motor900b
seuCarro.marcab = volkswagen

print(meuCarro.modelo,meuCarro.marcab.nomeMarca, meuCarro.motorb.nomeMoto)
print(seuCarro.modelo,seuCarro.marcab.nomeMarca, seuCarro.motorb.nomeMoto)