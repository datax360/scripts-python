from random import randint
import emoji
print(f'{'=-'*40}\nVou pensar em um numero entre 1 e 5, tente adivinhar qual numero estou pensando\n{'=-'*40}')
n = int(input('Digite um numero: '))
numeros = randint(1,5)
if n == numeros:
    print(f'{emoji.emojize(':sparkles:')} Parabens você acertou! {emoji.emojize(':sparkles:')}')
else:
    print('Que pena, não foi dessa vez ):')
