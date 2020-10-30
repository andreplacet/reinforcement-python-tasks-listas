# Exercicio 03

notas = []

for _ in range(4):
    nota = float(input(f'Informe a {_ + 1}º nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f'Notas digitadas')

for _ in range(len(notas)):
    print(f'{notas[_]}', end=' ')

print(f'\nMédia {media:.1f}')
