# Exercicio 21

listaCarro = []
listaConsumo = []

while len(listaCarro) < 5:
    listaCarro.append(input('Digite o nome do carro: '))
    listaConsumo.append(float(input('Digite o consumo do carro (km por litro): ')))
    print('novos dados inseridos\n')

results = ''
valor_gas = 2.25
total_km = 1000

for j, c in enumerate(listaCarro):
    print('Veiculo {}'.format(j+1))
    print('Nome: {}'.format(c))
    print('Km por litro: {}\n'.format(listaConsumo[j]))

    consumo_l = round(total_km/listaConsumo[j], 2)
    results += f'O carro {c} consume {consumo_l}L e custará $R{round(consumo_l*valor_gas, 2)} quando fizer {total_km}km\n'

print(f'O carro mais economico é o {listaCarro[listaConsumo.index(max(listaConsumo))]}')
print(results)
