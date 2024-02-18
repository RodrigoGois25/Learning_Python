#Crie um programa
#que leia o nome de uma
#cidade e diga se ela
#começa ou não com o
#nome "Santo"

#cidade=str(input('Digite o nome da sua Cidade: ')).strip().capitalize()
#divisao=cidade.split()
#teste=((divisao[0].find('Santo')))

#if teste == -1:
    #print('Essa cidade não começa com Santo')
#else:
    #print('Essa cidade começa com Santo')
cidade=str(input('Digite a cidade que você nasceu: ')).strip().capitalize()
print(cidade[:5]=='Santo')
