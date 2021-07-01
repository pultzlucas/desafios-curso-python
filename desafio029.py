vel = int(input('Qual a velocidade atual do carro? '))
maxVel = 80

if vel > 80:
    ticketValue = (vel - 80) * 7
    print(f'Multado! Você excedeu o limite permitido que é de 80Km/h você deve pagar uma multa de R${ticketValue},00')

print('Tenha um bom dia! Dirija com segurança!')
