from random import randint
from time import sleep
numero = randint(1,5)
escolhido = int(input('\033[4;31;40mInsira um número de 1 a 5\033[m'))
print ('\033[4;31;40mProcessando...\033[m')
sleep(3)
if escolhido == numero:
    print('\033[4;31;40mvocê acertou, o número escolhido pela maquina foi: {}\033[m'.format(numero))
else:
    print('\033[4;31;40mVocê errou, o número escolhido pela maquina foi: {}\033[m'.format(numero))
