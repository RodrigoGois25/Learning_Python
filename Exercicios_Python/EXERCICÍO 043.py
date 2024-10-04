###Cáculo de IMC###
peso=float(input('Digite seu Peso: '))
altura=float(input('Digite sua Altura, em metros: '))
imc=peso/(altura)**2

print('Seu IMC foi igual a {}'.format(round(imc, 2)))
if imc<18.5:
    print('Abaixo do peso!')
'''elif  18.5 >= 25:
    print('Peso ideal')
elif:
    
elif:
    
else:
    print('Obesidade mórbida')'''