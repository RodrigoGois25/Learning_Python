print('Multa de Trânsito')
vel=int(input('Digite a velocidade de seu carro: '))
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('O valor da sua muta será de R${:.2f}'.format((vel-80)*7))

print('Tenha um bom dia! Dirija com segurança!')