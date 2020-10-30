# Exercicio 14

perguntas = ['Telefonou para a vitima?', 'Esteve no local do crime?', 'Mora perto da vitima?',
             'Devia para a vitima?', 'Ja trabalhou com a vitima?']
resultado = []

print('Responda cada pergunta com [S]im ou [N]ão!')
for pergunta in perguntas:
    resposta = str(input(f'{pergunta} '))
    resultado.append(resposta[0])

resposta = resultado.count('s')

if resposta == 2:
    print('suspeito')
elif 3 <= resposta <= 4:
    print('cumplice')
elif resposta == 5:
    print('Assassino')
else:
    print('Inocente')
