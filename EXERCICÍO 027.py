#Faça um programa
#que leia o nome
#completo de uma
#pessoa, mostrando em
#seguida o primeiro e o
#último nome separadamente

nome=input('Digite seu nome completo: ').strip().title()
print('Olá {}'.format(nome))
n=nome.split()
print('Primeiro nome: {}'.format(n[0]))
print('Último nome é {}'.format(n[len(n)-1]))
print(n[len(n)-1])
#[len(n)] vai contar quantos nomes vão ter dentro da string dividida
#e o -1 serve para limitar ao último nome
#Mostre dentro de n o última palavra dessa lista