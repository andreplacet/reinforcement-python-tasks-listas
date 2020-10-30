# Exercicio 07

lista = []
soma = 0
multi = 1

for _ in range(5):
    valor = int(input('Digite um valor: '))
    lista.append(valor)

for _ in range(len(lista)):
    soma += lista[_]
    multi *= lista[_]

print(f'A soma dos valores digitados é: {soma}')
print(f'A multiplicação dos valores digitados é: {multi}')