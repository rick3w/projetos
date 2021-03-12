class ValidadorCPF:
    def __init__(self):
        self.cpf = input('\nDigite o cpf: ')
        self.cpf2 = ''

    def novo_cpf(self):
        for d in self.cpf[:-2]:
            if d.isdigit():
                self.cpf2 += d

    def digito_10(self):
        cont = 10
        total = 0
        for d in self.cpf2:
            total += int(d) * cont
            cont -= 1
        dig_10 = total * 10 % 11
        self.cpf2 += str(dig_10)

    def digito_11(self):
        cont = 11
        total = 0
        for d in self.cpf2:
            total += int(d) * cont
            cont -= 1
        dig_11 = total * 10 % 11
        self.cpf2 += str(dig_11)

    def validador(self):
        self.novo_cpf()
        self.digito_10()
        self.digito_11()

    def resultado(self):
        self.validador()
        if self.cpf == self.cpf2:
            print('O cpf é VÁLIDO!')
        else:
            print('O cpf é INVÁLIDO!')

cpf = ValidadorCPF()
cpf.resultado()
