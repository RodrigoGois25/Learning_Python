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

triangulo=a+b>c and b+c>a and a+c>b

if triangulo==True:
    print('É possível fazer um triângulo com esses valores!')
    
    if a==b==c:
        print('Este é um triângulo Equilátero!')    
    elif a==b!=c or b==c!=a or a==c!=b:
        print('Este é um triângulo Isoceles!')
    else:
        print('Este é um triângulo Escaleno!')

else:
    print('Não é possível fazer um triângulo com esses valores')

