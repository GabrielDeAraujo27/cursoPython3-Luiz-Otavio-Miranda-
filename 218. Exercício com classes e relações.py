class marca:
    def __init__(self, nomeMarca, nacionalidade):
        self.nomeMarca = nomeMarca
        self.nacionalidade = nacionalidade

    def defineMarca(self):
        self.nomeMarca = 'Honda' #input('Qual o nome da marca? ')
        self.nacionalidade = 'Americano' #input('Qual a nacionalidade desse carro? ')
        return self

class motor:
    def __init__(self, nomeMotor='', potencia=''):
        self.nomeMotor = nomeMotor
        self.potencia = potencia

    def defineMotor(self):
        self.nomeMotor = '900b' #input('Qual o nome desse motor? ')
        self.potencia = '70 cavalos' #input('Qual a potencia desse motor? ')
        return self

class carro:
    def __init__(self, nome='', marcab='', motorb=''):
        self.nome = nome
        self.marcab = marcab
        self.motorb = motorb
    def defineCarro(self):
        self.nome = 'Sedan' #input('Qual a nome desse carro? ')
        self.motorb = motor.defineMotor(self)
        self.marcab = marca.defineMarca(self)
        return self
meuCarro = carro()
meuCarro = carro.defineCarro(meuCarro)

print(meuCarro.nome)

print(meuCarro.marcab.nomeMarca)
print(meuCarro.marcab.nacionalidade)

print(meuCarro.motorb.nomeMotor)
print(meuCarro.motorb.potencia)
