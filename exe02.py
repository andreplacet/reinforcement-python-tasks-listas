# Exercicio 02

lista = []

for _ in range(10):
    n = float(input(f'Digite um {_ + 1}º número: '))
    lista.append(n)

for _ in range(len(lista)):
    print(lista[_], end=', ')
