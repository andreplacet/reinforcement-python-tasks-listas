# Exercicio 05

par = []
impar = []

for _ in range(20):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f'Pares: {par}\nImpares: {impar}')
