###Conversor de Bases Númericas###

num=(int(input('Digite um número inteiro: ')))
print(' ')
escolha=int(input('Base de Conversão\n - 1 para binário\n - 2 para octal\n - 3 para hexadecimal\n Digite a base escolhida: '))
print(' ')
if escolha == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida. Tente Novamente.')
    
###[ 2: ] Para mostrar apenas do terceiro digito em diante (fatiamento de string)### 