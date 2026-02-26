a = float(input('Qual o primeiro segmento? '))
b = float(input('Qual o segundo segmento? '))
c = float(input('Qual o terceiro segmento? '))
if a + b > c and a + c > b and b + c > a:
    print('Esses segmentos formam um triangulo')
else:
    print('Esses segmentos não formam um trangulo')
