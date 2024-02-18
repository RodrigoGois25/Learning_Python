#from random import choice
#print('Descubra um número, entre 1 e 5, que o computador escolheu')
#n=int(input('Digite o número: '))
#sorte=[1,2,3,4,5]
#escolhido=choice(sorte)
#print('O número sorteado foi {}'.format(escolhido))
#print('Parabéns, você acertou' if n==escolhido else 'Quase, tente novamente')


from random import randint
from time import sleep
computador = randint(0,5)
print('-=-' *20)
print('Vou pensaar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' *20)
jogador=int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador==computador:
    print('PARAÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))