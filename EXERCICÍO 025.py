#Crie um programa
#que leia o nome de uma
#pessoa e diga se ela
#tem "Silva" no nome

nome=str(input('Digite seu nome completo: ')).strip().capitalize() 
procura=('Silva' in nome)
if (procura) == True:
     print('Seu nome tem Silva')
else:
   print('Seu nome não tem Silva')
