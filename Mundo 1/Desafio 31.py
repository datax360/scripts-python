v = int(input('Qual a distancia da viagem? '))
if v <= 200:
    print(f'Sua viagem vai custar R${v*0.50:.2f}')
else:
    print(f'Sua viagem vai custar R${v*0.45:.2f}')
