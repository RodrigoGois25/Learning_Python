print('Tinta necessária para pintar uma parede, sabendo que cada L de tinta pinta uma área de 2m² ')
h=float(input('Digite a altura da parede: '))
l=float(input('Digite a largura da parede: '))
a=h*l
print(' A quantidade de tinta necessária para pintar essa parede é {:.2f}L'.format(a/2))