'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

import math

cat_op = float(input('digite o cateto oposto: '))
cat_ad = float(input('digite o cateto adjacente: '))

print(f'hipotenusa é {math.hypot(cat_ad, cat_op):.2f}')


'''hipotenusa = math.sqrt((math.pow(cat_op, 2)+math.pow(cat_ad, 2)))
print(f'a hipotenusa é {hipotenusa:.2f}')'''