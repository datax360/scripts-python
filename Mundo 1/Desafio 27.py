n = str(input('Diga seu nome: ')).strip().title()
n = n.split()
print(f"""Seu primeiro nome é {n[0]}
Seu ultimo nome é {n[len(n)-1]}""")