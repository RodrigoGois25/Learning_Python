print('=-=-'*20)
print('Dá pra formar um triângulo usando 3 valores aleatorios ?')
print('=-=-'*20)
#Conceito matemático: A soma de dois lados é sempre menor que o terceiro lado
#a+b>c
#b+c>a
#a+c>b
a=float(input('Digite um valor: '))
print(' ')
b=float(input('Digite um valor: '))
print(' ')
c=float(input(' Digite um valor: '))
print(' ')

if a+b>c and b+c>a and a+c>b:
    print('É possível fazer um triângulo com esses valores')
else:
    print('Não é possível fazer um triângulo com esses valores')



