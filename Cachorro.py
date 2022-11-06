class Cachorro:
    def __init__(self, nome, peso, cor): #parâmetros

        #atributos
        self.nome = nome
        self.peso = peso
        self.cor = cor

    def latir(self):
        print('auuuuuu')

    def comer(self, quantidade):
        self.peso = self.peso + quantidade
        
luna=Cachorro('luna', 15, 'preto')
print(luna)
print(luna.nome)

# apolo=Cachorro('apolo',12,'branco')
# print(apolo)
# print(apolo.nome)

luna.latir()
print('peso da luna é ', luna.peso)
luna.comer(2)
print('peso novo da luna é ', luna.peso)
