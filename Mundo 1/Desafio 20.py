import random
n = str(input('Diga o primeiro nome: '))
n1 = str(input('Diga o segundo nome: '))
n2 = str(input('Diga o terceiro nome: '))
n3 = str(input('Diga o quarto nome: '))
lista = [n, n1, n2, n3]
random.shuffle(lista)
print(f'A ordem sera {lista}')
#Esse foi um saco