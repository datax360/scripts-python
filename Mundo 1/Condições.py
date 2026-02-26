n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print(f'A media aritmetica das notas é {(n1+n2)/2:.1f}')
if n1 and n2 >= 6:
    print('Parabens passou!')
else:
    print('Não passou!')
#Cores
print('\033[4:35mWOW')