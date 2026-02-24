import random
import emoji
n = str(input('Nome do primeiro aluno: '))
n1 = str(input('Nome do segundo aluno: '))
n2 = str(input('Nome do terceiro aluno: '))
n3 = str(input('Nome do quarto aluno: '))
print(f'O escolhido é {emoji.emojize(':sparkles:')}{random.choice([n, n1, n2, n3])}{emoji.emojize(':sparkles:')}')
