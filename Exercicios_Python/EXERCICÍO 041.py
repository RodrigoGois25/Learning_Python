from datetime import date
atual=date.today().year
ano=int(input('Digite o ano que você nasceu: '))
print(' ')
idade=atual-ano

if idade <= 9:
    print('Mirim')
elif idade >= 9 and idade <= 14:
    print('Infantil')
elif idade >= 14 and idade <= 19:
    print('Junior')
elif idade == 20:
    print('Sênior')
else:
    print('Master')
print(' ')
print('Você tem {} anos'.format(idade))