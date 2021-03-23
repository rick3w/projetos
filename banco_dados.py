class CarrinhoCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

class Produto:
    def __init__(self):
        self.nome = input('\nNome do produto: ')
        self.valor = input('Valor do produto: ')
