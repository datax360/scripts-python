from datetime import date
a = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')
