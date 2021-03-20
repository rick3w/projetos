class Cadastro:
    def __init__(self):
        while True:
            self.nome = input('\nNome: ').title().strip()
            if self.nome_valido():
                self.idade = input('Idade: ')
                if self.idade_valida():
                    print('\nCADASTRO EFETUADO COM SUCESSO!')
                    print(f'Você se chama {self.nome} e tem {self.idade} anos.')
                    print('\nFIM DO PROGRAMA.\n')
                    break
                else:
                    print('ERRO! Idade inválida.')
            else:
                print('ERRO! Nome inválido.')
        
    def nome_valido(self):
        nome = self.nome.replace(' ', '')
        if nome.isalpha():
            return True
        else:
            return False

    def idade_valida(self):
        try:
            idade = int(self.idade)
            return True
        except:
            return False

def titulo(titulo, tamanho):
    return f'\n{"-" * tamanho}\n{titulo:^{tamanho}}\n{"-" * tamanho}'