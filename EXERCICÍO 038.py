num1=int(input('Digite um valor: '))
num2=int(input('Digite outro valor: '))
maior=num1>num2
menor=num1<num2
if maior==True:
    print('{} é maior que {}'.format(num1, num2))
elif menor==True:
    print('{} é maior que {}'.format(num2,num1))
else:
    print('\033[34m Não existe valor maior, os dois são iguais\033[m')
    