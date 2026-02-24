n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
s = n1+n2
sub = n1-n2
mult = n1*n2
div = n1/n2
rest = n1%n2
exp = n1**n2
print('A soma é {},\na subtração é {} '.format(s, sub), end=', ')
print('\na multiplicação é {},\na divisão é {:.2f} o que sobra da divisão é {}\ne a exponenciação é {}'.format(mult, div, rest, exp))
