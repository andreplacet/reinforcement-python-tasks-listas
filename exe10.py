# Exercicio 10

lista_a = []
lista_b = []
lista_20 = []

for _ in range(10):
    n1 = int(input('Digite um número para a lista [A]: '))
    n2 = int(input('Digite um número para a lista [B]: '))
    lista_a.append(n1)
    lista_b.append(n2)

for _ in range(10):
    lista_20.append(lista_a[_])
    lista_20.append(lista_b[_])

print(f'Lista 1 {lista_a}\nLista 2 {lista_b}\nLista intercalada {lista_20}')
