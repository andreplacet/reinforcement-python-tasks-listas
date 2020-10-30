# Exercicio 11

lista_a = []
lista_b = []
lista_c = []
lista_20 = []

for _ in range(10):
    n1 = int(input('Digite um número para a lista [A]: '))
    n2 = int(input('Digite um número para a lista [B]: '))
    n3 = int(input('Digite um número para a lista [C]: '))
    lista_a.append(n1)
    lista_b.append(n2)
    lista_c.append(n3)

for _ in range(10):
    lista_20.append(lista_a[_])
    lista_20.append(lista_b[_])
    lista_c.append(lista_c[_])

print(f'Lista 1 {lista_a}\nLista 2 {lista_b}\nLista 3 {lista_c}\n'
      f'Lista intercalada {lista_20}')
