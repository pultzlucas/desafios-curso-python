n = int(input('Digite um número inteiro: '))
print('----- Tabuada -----')

for i in range(10 + 1):
    res = n * i
    print(f'{n} x {i} = {res}')