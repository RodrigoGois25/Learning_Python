###Forma de pagamento e acréscimo, em condição ao pagamento###
preço=float(input('Digite o preço do produto: '))
print(' ')

forma_de_pagamento=int(input('Forma de pagamento:\n 1 = Cartão\n 2 = Dinheiro\n 3 = Cheque\n Digite o número referente a forma de pagamento: '))

print(' ')

if forma_de_pagamento==1:
    
    parcelas=int(input('Digite em quantas parcelas você deseja pagar: '))
    calculadora_de_porcentagem=((preço*parcelas)/100)
    
    if parcelas == 1:
        print('Você ganhará um desconto de 5%, o valor do produto será R${} agora'.format(preço-(calculadora_de_porcentagem)))
    
    elif parcelas == 2:
        print('O valor será o mesmo, R${}'.format(preço))
    
    elif parcelas >=5:
        print('O valor total terá um acréscimo de 20%, o valor do produto será R${} agora, e você pagará em {} vezes de R${}'.format(preço+calculadora_de_porcentagem, parcelas, ((preço+calculadora_de_porcentagem)/parcelas)))

else:
    print('Você ganhará um desconto de 10%, o valor do produto será R${} agora'.format(preço-(preço/10)))
    
