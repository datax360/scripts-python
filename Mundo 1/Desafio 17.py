import emoji
import math
co = float(input('Diga o valor do cateto oposto: '))
ca = float(input('Diga o valor do cateto adjacente: '))
print(f'{emoji.emojize(':sparkles:')}A media da hipotenusa é {math.hypot(co, ca):.2f}{emoji.emojize(':sparkles:')}')
