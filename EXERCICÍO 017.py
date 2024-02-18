from math import hypot
ops=float(input('Digite o valor do cateto oposto ao ângulo: '))
adj=float(input('Digite o valor do cateto adjacente ao ângulo: ' ))
h=(ops**2+adj**2)**(1/2)
#h=hypot(ops, adj)
print('O valor da hipotenusa é {:.2f}'.format(h))