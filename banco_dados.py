class BancoDados:
    def __init__(self):
        self.cadastros = []

    def menu(self):
        self.titulo('TECH N GAMES', 50)
        while True:
            print('\nEscolha uma das opções a seguir:')
            print('[A] Cadastrar cliente\n[B] Apagar cliente')
            print('[C] Listar clientes cadastrados\n[D] Sair')
            opc = input('> ').upper().strip()
            if self.validar_string(opc) and opc in 'ABCD':
                if opc == 'A':
                    self.cadastrar_cliente()
                elif opc == 'B':
                    self.apagar_cliente()
                elif opc == 'C':
                    self.listar_clientes()
                else:
                    print('\nFIM DO PROGRAMA\n')
                    break
            else:
                print('ERRO! Opção inválida.')
    
    def cadastrar_cliente(self):
        nome = input('\nDigite o nome: ').title().strip()
        if self.validar_string(nome):
            idade = input('Digite a idade: ')
            if self.validar_numero(idade):
                self.cadastros.append({'nome': nome, 'idade': idade})
                print('CLIENTE CADASTRADO!')
            else:
                print('ERRO! Idade inválida.')
        else:
            print('ERRO! Nome inválido.')

    def apagar_cliente(self):
        if len(self.cadastros) == 0:
            print('Não há nenhum cliente!')
        else:
            opc = input('\nQual cliente deseja apagar?\n> ')
            if self.validar_numero(opc) and int(opc) in range(len(self.cadastros) + 1):
                self.cadastros.pop(int(opc) - 1)
                print('CLIENTE APAGADO!')
            else:
                print('ERRO! Cliente não existe.')

    def listar_clientes(self):
        if len(self.cadastros) == 0:
            print('Não há nenhum cliente!')
        else:
            for cliente, dados in enumerate(self.cadastros):
                print('-' * 50)
                print(f'Cliente {cliente + 1}')
                print(f'Nome: {dados["nome"]}\nIdade: {dados["idade"]} anos')
            print('-' * 50)

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

    def titulo(self, titulo, tamanho):
        print()
        print(f'{"-" * tamanho}')
        print(f'{titulo:^{tamanho}}')
        print(f'{"-" * tamanho}')
