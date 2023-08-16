class lutador:
    def __init__(self):
        self._nome
        self._forca


    @property
    def nome(self):
        print('GETTER')
        return self._nome
    @nome.setter
    def nome(self, name=str):
        print('SETTER')
        self._nome = name


Ryu = lutador()
n = 'Ryu'
Ryu.nome('Ryu')
#print(Ryu.nome)
