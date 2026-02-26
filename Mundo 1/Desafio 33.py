a = int(input('Digite um primeiro valor: '))
b = int(input('Digite um segundo valor: '))
c = int(input('Digite um terceiro valor: '))
M = a
m = a
if b > c and b > a:
    M = b
if c > b and c > a:
    M = c
if b < c and b < a:
    m = b
if c < b and c < a:
    m = c
print(f'O maior valor é {M}\nO menor valor digitado foi {m}')
