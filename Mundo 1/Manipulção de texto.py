frase = 'Curso em Video Python'
print(frase[9::3])
#Fatiamento
print(len(frase))
print(frase.count(' ',0,9))
print(frase.find('ho'))#Procura pelo lado covencional de leitura, lado esquerdo
print(frase.rfind('ho'))#Procura a partir do lado direito(Right)
print('Python' in frase)
#Analise
print(frase.replace('Python','Guanabara'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase2 ='    Aprenda Python    '
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())
#Transformação
print(frase.split())
print(frase[0], frase[len(frase)-1])
#Divisão e Junção
