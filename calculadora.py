class Calculadora:
    def __init__(self):
        while True:
            try:
                self.n1 = int(input('\nDigite o 1 número: '))
                self.op = input('Digite o operador: ')
                self.n2 = int(input('Digite o 2 número: '))
            except:
                print('ERRO! Tente novamente.')
            else:
                break
    
    def adição(self):
        print(self.n1 + self.n2)
    
    def subtração(self):
        print(self.n1 - self.n2)

    def multiplicação(self):
        print(self.n1 * self.n2)

    def divisão(self):
        print(self.n1 / self.n2)

    def resultado(self):
        print('Resultado: ', end='')
        if self.op == '+':
            self.adição()
        elif self.op == '-':
            self.subtração()
        elif self.op == '*':
            self.multiplicação()
        elif self.op == '/':
            self.divisão()
        
calc = Calculadora()
calc.resultado()
