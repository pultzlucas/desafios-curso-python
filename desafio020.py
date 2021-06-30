from random import shuffle

studentsName = []

for n in range(4):
    name = input(f'Nome do aluno {n + 1}: ')
    studentsName.append(name)

apresentationSort = expovariate(studentsName)
print(apresentationSort)