s = float(input('Qual o salario? R$'))
if s >= 1250:
    print(f'O salario passa a ser R${s+(s*10/100):.2f}')
else:
    print(f'O salario passa a ser R${s+(s*15/100):.2f}')
