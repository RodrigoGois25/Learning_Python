print('Aumento de Salário')
salario=float(input('Digite o valor do seu salário: R$'))
if salario >= 1250:
    novo=((salario*0.1)+salario)
else:
    novo=((salario*0.15)+salario)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, novo))