# Exercicio 09

lista = []
lista_quadrado = []

for _ in range(10):
    n = int(input('Digite um número: '))
    lista.append(n)

for _ in range(len((lista))):
    n = lista[_]
    n *= n
    lista_quadrado.append(n)

print(f'Lista {lista}')
print(f'Lista ao quadrado {lista_quadrado}')
