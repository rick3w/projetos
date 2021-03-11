cpf = input('Digite o cpf: ')
novo_cpf = ''

for d in cpf[:-2]:
    if d.isdigit():
        novo_cpf += d

cont_1 = 10
cont_2 = 11
total_1 = 0
total_2 = 0

for d in novo_cpf:
    total_1 += int(d) * cont_1
    cont_1 -= 1

digito_10 = total_1 * 10 % 11
novo_cpf += str(digito_10)

for d in novo_cpf:
    total_2 += int(d) * cont_2
    cont_2 -= 1

digito_11 = total_2 * 10 % 11
novo_cpf += str(digito_11)

if cpf == novo_cpf:
    print('O cpf é VÁLIDO!')
else:
    print('O cpf é INVÁLIDO!')
