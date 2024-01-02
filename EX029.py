'''Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input('qual a velocidade que seu carro passou na via?: '))

if velocidade>80:
    print(f'você ultrapassou {velocidade-80}km/h além do limite.')
    print(f'você foi multado em R${(velocidade-80)*7}, cada Km acima do limite custa R$7,00.')
else:
    print('você respeitou as leis e não será multado.')