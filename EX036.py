'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor_casa = float(input('qual o valor da casa?: '))
salario = float(input('qual o valor do seu salário?: '))
anos = int(input('em quantos anos você irá pagar?: '))

prest = valor_casa/(anos*12)
if prest>(salario*0.3):
    print('infelizmente o empréstimo foi negado.')
else:
    print('empréstimo aceito!')