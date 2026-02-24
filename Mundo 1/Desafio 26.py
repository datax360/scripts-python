n = str(input('Digite uma frase: ')).strip().upper()
print(f"""A letra A aparece {n.count('A')} vezes
A primeira letra A aparece na posição {n.find('A')+1}
A ultima letra A aparece na posição {n.rfind('AA')+1}""")