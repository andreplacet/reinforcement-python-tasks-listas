# Exercicio 12

altura = []
idade = []

for i in range(30):
    idade.append(int(input(f"Digite a idade do {i + 1}º aluno: ")))
    altura.append(float(input(f"Digite a altura do {i + 1}º aluno: ")))

media_altura = sum(altura) / len(altura)
c = 0
quantidade = 0

while c < len(idade):
    if idade[c] > 13 and altura[c] < media_altura:
        quantidade += 1
    c += 1
print(f"Quantidade de Alunos com mais de 13 amos com altura inferior a media: {quantidade}")
