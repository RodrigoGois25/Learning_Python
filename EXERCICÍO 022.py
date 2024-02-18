###022:crie um programa
#que leia o nome
#completo de uma
#pessoa e mostre:

#>O nome com todas as
#letras maiúsculas

#>O nome com todas
#minúsculas

#>Quantas letras ao
#todo (sem considerar
#espaços)

#>Quantas letras tem o
#primeiro nome

nome=str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas fica assim: {}'.format(nome.upper()))
print('Seu nome em minúsculas fica assim: {}'.format(nome.lower()))
separa=(nome.split())
#todas=(''.join(teste))
#print((teste))
#print('A palavra digitada tem um total de {} letras'.format(len(todas)))
print('A primeira palavra da frase digitada tem {} letras'.format(len(separa[0])))



