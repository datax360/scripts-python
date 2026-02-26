v = float(input('Qual a velocidade do  seu carro? '))
if v <= 80:
    print('Sua velocidade esta dentro do permitido, continue dirigindo com segurança!')
else:
    print(f'Sua velocidade esta acima do permitido, sua multa é de R${(v-80)*7}')
