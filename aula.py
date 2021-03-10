cpf = input('Digite o cpf: ')
novo_cpf = ''

for d in cpf:
    if d.isdigit():
        novo_cpf += d

