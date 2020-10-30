# Exercicio 06

alunos = {}
notas = []
alunos_aprovados = 0

for _ in range(10):
    aluno = str(input('Nome do Aluno: ')).capitalize()
    for _ in range(4):
        nota = float(input(f'Informe a {_ + 1}º nota: '))
        notas.append(nota)
    alunos[f'{aluno}'] = notas.copy()
    notas.clear()


for item in alunos.values():
    media = sum(item) / len(item)
    if media >= 7:
        alunos_aprovados += 1

print(f'O total de alunos com média maior que 7 é {alunos_aprovados}')
