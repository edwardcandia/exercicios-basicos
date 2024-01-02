import math
import random
n = random.randint(1,5)

num_usuario = int(input('digite um número de 1 a 5 e veja se você acertou: '))

while num_usuario != (1 and 2 and 3 and 4 and 5):
    num_usuario = int(input('digite um número de 1 a 5 e veja se você acertou: '))

if num_usuario>5 or num_usuario<1:
    print('DE 1 A 5 ANIMAL!')

elif num_usuario == n:
    print(f'parabéns, você acertou, o número é {num_usuario}')
else:
    print(f'você errou, o número era {n} e você digitou {num_usuario}.')