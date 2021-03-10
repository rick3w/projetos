from PySimpleGUI import *

layout = [
    [Text('OLÁ MUNDO!')],
    [Text('Usuário'), Input(key='user')],
    [Text('Senha'), Input(key='pass', password_char='*')],
    [Button('LOGAR')],
    [Button('SAIR')]
]

login1 = [
    [Text('LOGADO COM SUCESSO!')]
]

login2 = [
    [Text('ERRO!')]
]

janela = Window('PROGRAMA TESTE', layout=layout)
