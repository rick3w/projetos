class Cadastro:
    def __init__(self):
        while True:
            self.nome = input('\nNome: ').title().strip()
            if self.validar_nome():
                self.idade = input('Idade: ')
                if self.validar_idade():
                    print('\nCADASTRO EFETUADO COM SUCESSO!')
                    print(f'Você se chama {self.nome} e tem {self.idade} anos.')
                    print('\nFIM DO PROGRAMA.\n')
                    break
                else:
                    print('ERRO! Idade inválida.')
            else:
                print('ERRO! Nome inválido.')
        
    def validar_nome(self):
        nome = self.nome.replace(' ', '')
        if nome.isalpha():
            return True
        else:
            return False

    def validar_idade(self):
        try:
            idade = int(self.idade)
            return True
        except:
            return False

def titulo(titulo, tamanho):
    return f'\n{"-" * tamanho}\n{titulo:^{tamanho}}\n{"-" * tamanho}'
