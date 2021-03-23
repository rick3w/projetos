class BancoDados:
    def __init__(self):
        self.cadastros = []

    def menu(self):
        self.titulo('TECH N GAMES', 50)
        while True:
            print('\nEscolha uma das opções a seguir:')
            print('[A] Cadastrar pessoa\n[B] Listar pessoas cadastradas\n[C] Sair')
            opc = input('> ').upper().strip()
            if self.validar_string(opc) and opc in 'ABC':
                if opc == 'A':
                    self.cadastrar_pessoa()
                elif opc == 'B':
                    self.listar_cadastros()
                else:
                    print('\nFIM DO PROGRAMA\n')
                    break
            else:
                print('ERRO! Opção inválida.')
    
    def cadastrar_pessoa(self):
        while True:
            nome = input('\nDigite o nome: ').title().strip()
            if self.validar_string(nome):
                idade = input('Digite a idade: ')
                if self.validar_numero(idade):
                    self.cadastros.append({'nome': nome, 'idade': idade})
                    print('CADASTRO EFETUADO!')
                    break
                else:
                    print('ERRO! Idade inválida.')
            else:
                print('ERRO! Nome inválido.')

    def validar_string(self, string):
        string = string.replace(' ', '')
        if string.isalpha():
            return True
        else:
            return False

    def validar_numero(self, numero):
        try:
            numero = int(numero)
            return True
        except:
            return False

    def listar_cadastros(self):
        if len(self.cadastros) == 0:
            print('Não há nenhum cadastro!')
        else:
            for cliente, dados in enumerate(self.cadastros):
                print(f'\nCliente {cliente + 1}:')
                print(f'Nome: {dados["nome"]}\nIdade: {dados["idade"]}')

    def titulo(self, titulo, tamanho):
        print()
        print(f'{"-" * tamanho}')
        print(f'{titulo:^{tamanho}}')
        print(f'{"-" * tamanho}')
