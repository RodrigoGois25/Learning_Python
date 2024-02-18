n1=float(input('Digite sua primeira nota: '))
print(' ')
n2=float(input('Digite sua segunda nota: '))

media=(n1+n2)/2
reprovado=media<5.0
recuperaçao=media<=5.0 or media <= 6.9
aprovado=media<=7.0
print(' ')
print('Sua média entre {} e {} foi de {:.1f} pontos.'.format(n1, n2 ,media))
print(' ')
if reprovado == True:
    print('Reprovado')
elif recuperaçao == True:
    print('Recuperação')
elif media > 10:
    print('Notas inválidas, tente novamente')
else:
    print('Aprovado')

print(' ')

