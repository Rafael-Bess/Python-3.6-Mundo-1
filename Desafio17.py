#Faça um programa que leia os comprimento do cateto oposto e do cateto adjacente de um triângulo e retângulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
co = float(input('\033[4;30;41mInforme o comprimento do cateto oposto:\033[m'))
ca = float(input('\033[4;30;41mInforme o comprimento do cateto adjacente:\033[m'))
hi = float(hypot(co, ca))
print('\033[4;30;41mO comprimento da hipotenusa é {:.2f}\033[m'.format(hi))

# no import acima como usei apenas o HYPOT da biblioteca math é possivel importar apenas ele
'''
co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('O resultado da Hipotenusa é {:.2f}'.format(hi)
o calculo da hipotenusa é cateto oposto elevado a 2 + cateto adjascente elevado a 2 o resultado é a raiz quadrado desse calculo é a hipotenusa
'''
