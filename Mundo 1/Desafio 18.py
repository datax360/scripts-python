from math import radians, sin, cos, tan
n =  float(input('Diga um angulo: '))
print(f'{'='*30}\nO SENO desse angulo é {sin(radians(n)):.2f}\nO COSSENO desse angulo é {cos(radians(n)):.2f}\nA TANGENTE desse numero é {tan(radians(n)):.2f}\n{'='*30}')
