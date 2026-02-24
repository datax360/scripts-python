n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
p1 = 2
p2 = 3
print(f'A media aritmetica das notas é {(n1+n2)/2:.1f}')
print(f'A media ponderada das notas é {(n1*p1+n2*p2)/p1+p2:.1f}')
