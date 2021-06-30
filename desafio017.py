from math import pow, sqrt

catetoOpo = float(input('Digite o valor do cateto oposto: '))
catetoAdj = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = sqrt(pow(catetoOpo, 2) + pow(catetoAdj, 2))

print('Valor da hipotenusa é:', hipotenusa)