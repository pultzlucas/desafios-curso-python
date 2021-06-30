from random import choice

studentsName = []

for n in range(4):
    name = input(f'Nome do aluno {n + 1}: ')
    studentsName.append(name)

chosenStudent = choice(studentsName)
print('O aluno escolhido é:', chosenStudent)