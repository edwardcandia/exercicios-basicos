'''Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

import math

angulo = float(input('digite o ângulo desejado: '))

print(f'\nângulo: {angulo}\nseno: {math.sin(math.radians(angulo))}\ncosseno: {math.cos(math.radians(angulo))}\ntangente: {math.tan(math.radians(angulo))}')