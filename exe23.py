# Exercicio 23

from random import randrange

lancamentos = []

for i in range(100):
    lancamentos.append(randrange(1, 6 + 1))

for i in range(6):
    print(f"O número {i + 1} foi gerado {lancamentos.count(i + 1)} vezes")

