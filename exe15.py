# Exercicio 15

lista = []
media_acima = []
media_abaixo = []

print('Para finalizar o programa digite -1')
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    else:
        lista.append(n)

print(f'Quantidade de números digitado: {len(lista)}\n'
      f'Valores digitado: {lista}')

print('Valores digitados na ordem inversa')
for _ in lista[::-1]:
    print(_)

print(f'Soma dos valores digitados: {sum(lista)}\n'
      f'Média dos valores digitados: {sum(lista) / len(lista):.1f}')

for _ in lista:
    if _ > sum(lista) / len(lista):
        media_acima.append(_)
    else:
        media_abaixo.append(_)

print(f'Valores acimda de média: {media_acima}\n'
      f'Valores abaixo da média: {media_abaixo}')

print('A vingança nunca é plena, mata a alma e a envenena')
