nome =  str(input('Digite seu nome completo: ')).strip()
sep = nome.split()
print(f"""Nome em maiusculo: {nome.upper()}
Nome em minusculo: {nome.lower()}
O nome tem {len(nome)-nome.count(' ')} letras
Seu primeiro nome é {sep[0]} e ele tem {len(sep[0])} letras""")
