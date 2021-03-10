from random import randint

class ChuteONumero:
    def __init__(self):
        self.chute = 0
        self.aleatorio = 0

    def Iniciar(self):
        self.GerarNumAleatorio()
        while True:
            self.NumChute()
            if self.chute > self.aleatorio:
                print('Chute um valor menor')
            elif self.chute < self.aleatorio:
                print('Chute um valor maior')
            elif self.chute == self.aleatorio:
                print('\nPARABÉNS! Acertou na mosca')
                break
    
    def GerarNumAleatorio(self):
        self.aleatorio = randint(1, 100)

    def NumChute(self):
        self.chute = int(input('\nChute um número: '))

chute = ChuteONumero()
chute.Iniciar()
