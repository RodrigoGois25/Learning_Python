'''import datetime
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime('%Y')'''

from datetime import date
atual=date.today().year
ano=int(input('Informe seu ano de nascimento: '))
print(' ')
idade_atual=atual-ano

futuro = idade_atual < 18
presente = idade_atual == 18

print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade_atual, atual))
print(' ')

if futuro == True:
    saldo = 18 - idade_atual
    print('Terá que se alistar daqui a {} anos.'.format(saldo))

elif presente == True:
    print('Chegou a hora de se alistar ao Exército Brasileiro!'.format(saldo))

else:
    saldo = idade_atual - 18
    print('Você deveria ter se alistado há {} anos, caso não tenha se alistado.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi {}'.format(ano))
    