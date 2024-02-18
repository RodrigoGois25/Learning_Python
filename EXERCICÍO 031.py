print('Preço das Passagens')
km=(int(input('Digite o valor de quilômetros percorridos: ' )))
print('Você está prestes a começar uma viagem de {}Km.'.format(km))
if km <= 200:
    print('O valor da sua viagem ficou R${:.2f}'.format(km*0.5))
else:
    print('O valor da viagem ficou R${:.2f}'.format(km*0.45))
#print('Nossa fórmula para calcular:\n km>200 = (km*0,45)\n km<200 = (km*0,50)')
print('Obrigado por viajar conosco!')    