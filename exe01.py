# Exercicio 01

lista = []

for _ in range(5):
    n = int(input('Digite um número: '))
    lista.append(n)

for _ in range(len(lista)):
    print(lista[_], end=' ')
