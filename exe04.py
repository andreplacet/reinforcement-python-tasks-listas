# Exercicio 4

consoantes = []

for _ in range(10):
    caracter = str(input(f'Digite o {_ + 1}º caracter para verificar consoantes: ')).lower()
    if caracter not in ('a', 'e', 'i', 'o', 'u'):
        consoantes.append(caracter)

print('Consoantes digitadas')

for _ in range(len(consoantes)):
    print(f'{consoantes[_]}', end=' ')
