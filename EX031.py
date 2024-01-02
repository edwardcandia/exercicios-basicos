'''Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

distancia = float(input('qual a distancia da viagem?(em Km):'))
if distancia<=200:
    passagem = distancia * 0.50
    print(f'valor da passagem é: R${passagem:.2f}')
else:
    passagem = distancia * 0.45
    print(f'valor da passagem é: R${passagem:.2f}')