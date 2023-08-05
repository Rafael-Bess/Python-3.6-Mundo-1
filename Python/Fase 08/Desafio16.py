#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira Ex: Digite um número: 6.127 O número 6.127 tem a parte Inteira 6. Utilizar MATH

from math import trunc
num = float(input('\033[4;31;40mDigite um número:\033[m'))
int = trunc(num)
print('\033[4;31;40mO número \033[4;31;40m{} tem a parte inteira {}\033[m'.format(num, int))


'''
num = float(input('Digite um número: '))
print('O valor digitado é {} e a sua porção inteira é {}'.format(num, int(num)))
'''