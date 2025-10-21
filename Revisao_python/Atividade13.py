alunos = [{"nome": "Ana", "nota": 7},{"nome": "Beto", "nota": 9},{"nome": "Carlos", "nota": 5}]
aprovados = []

for aluno in alunos:
    if aluno["nota"] >= 7:
        aprovados.append(aluno["nome"])

print(aprovados)