class BancoDados:
    def __init__(self):
        self.cadastros = {}
    
    def cadastrar_pessoa(self):
        while True:
            nome = input('\nDigite o nome: ').title().strip()
            if self.validar_string(nome):
                idade = input('Digite a idade: ')
                if self.validar_numero(idade):
                    self.cadastros = {nome, idade}
                    print('\nCADASTRO EFETUADO!')
                    while True:
                        resp = input('\nDeseja cadastrar mais pessoas? [S/N]: ').upper().strip()
                        if self.validar_string(resp) and resp in 'SN':
                            break
                        else:
                            print('ERRO! Resposta inválida.')
                    if resp == 'N':
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
