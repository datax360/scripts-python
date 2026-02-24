num = int(input('Diga um numero: '))
print(f"""Unidade: {num // 1 % 10}
Dezena: {num // 10 % 10}
Centena: {num // 100% 10}
Milhar: {num // 1000 %10}""")