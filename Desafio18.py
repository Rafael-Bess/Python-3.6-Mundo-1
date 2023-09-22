'''Faca um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
angulo = float(input('Digite o Angulo: '))
angulorad = math.radians(angulo)
seno = math.sin(angulorad)
cosseno = math.cos(angulorad)
tangente = math.tan(angulorad)
print('O seno do angulo {:.2f} é: {:.2f}'.format(angulo, seno))
print('O cosseno do angulo {:.2f} é: {:.2f}'.format(angulo, cosseno))
print('A tangente do angulo {:.2f} é: {:.2f}'.format(angulo, tangente))'''

'''Faca um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
Pode ser utilizado também somente com o from e utilizando as formas de calculos que usei
from math import radians, sin, cos, tan
angulo = float(input('Digite o Angulo: '))
angulorad = radians(angulo)
seno = sin(angulorad)
cosseno = cos(angulorad)
tangente = tan(angulorad)
print('O seno do angulo {:.2f} é: {:.2f}'.format(angulo, seno))
print('O cosseno do angulo {:.2f} é: {:.2f}'.format(angulo, cosseno))
print('A tangente do angulo {:.2f} é: {:.2f}'.format(angulo, tangente))
'''

#{'limpa':'\033[m',


#Refiz o código e a forma mais optimizadas foram essas.
from math import sin, cos, tan, radians
cores = {'limpa':'\033[m',
         'Azul':'\033[1;34;40m',
         'a': '\033[1;30;44]'
}
angulo = float(input('Digite o seu Angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno é: {}{:.2f}{}\nO cosseno é: {}{:.2f}{}\nA tangente é: {}{:.2f}{}'.format(
    cores['Azul'], seno, cores['limpa'],
    cores['Azul'], cosseno, cores['limpa'],
    cores['Azul'], tangente, cores['limpa']
))
