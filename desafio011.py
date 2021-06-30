x = float(input('Largura da parede em metros: '))
y = float(input('Altura da parede em metros: '))
litersByMeter = float(input('Litros de tinta por metro: '))

area = x * y
inkQuant = area * litersByMeter

print(f'Quantidade de tinta necessaria: {inkQuant} L')
