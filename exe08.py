# Exercicio 08

pessoa = []

for _ in range(5):
    nome = str(input('Nome: '))
    idade = int(input('Idade:'))
    altura = float(input('Altura: '))
    pessoa.append(nome)
    pessoa.append(idade)
    pessoa.append(altura)

for _ in range(len(pessoa)):
    print(f'{pessoa[_]}')
