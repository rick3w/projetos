def real(valor):
    """
    Converte o valor informado para formatação em real (R$).
    """
    return f'R$ {valor:.2f}'.replace('.', ',')
