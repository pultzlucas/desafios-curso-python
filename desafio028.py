from random import randint

guess = randint(0, 10)
print('Pensei em um número entre 0 e 10...Tente adivinhar!')

attempt = int(input('Digite sua resposta: '))

if attempt == guess:
    print('Muito bem você acertou!')
else:
    print('Ganhei! A resposta era', guess)