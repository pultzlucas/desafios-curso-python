from random import shuffle

studentsName = []

for n in range(4):
    name = input(f'Nome do aluno {n + 1}: ')
    studentsName.append(name)

shuffle(studentsName)
print('A ordem de apresentação é:',studentsName)