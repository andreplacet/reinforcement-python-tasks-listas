# Exercicio 17

atletas = {}
saltos = []

while True:
    nome = str(input('Nome do atleta: ')).capitalize()
    if not nome:
        break
    else:
        for _ in range(5):
            salto = float(input(f'Valor do {_ + 1} salto: '))
            saltos.append(salto)
    atletas[f'{nome}'] = saltos

for k, v in atletas.items():
    print(f'Nome do Atleta: {k}\n'
          f'Primeiro Salto: {v[0]}\n'
          f'Segundo Salto: {v[1]}\n'
          f'Terceiro Salto: {v[2]}\n'
          f'Quarto Salto: {v[3]}\n'
          f'Quinto salto: {v[4]}\n')
    print(f'Resultado final:\n'
          f'Atleta: {k}\n'
          f'Saltos: {v}\n'
          f'Media dos saltos: {sum(v) / len(v):.1f}\n')
