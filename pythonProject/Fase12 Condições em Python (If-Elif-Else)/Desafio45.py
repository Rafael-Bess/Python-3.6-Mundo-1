import random
from time import sleep
eu = int(input('Vamos jogar Jo-ken-pô?\n'
            '1 - Pedra\n'
            '2 - Papel\n'
            '3 - Tesoura\n'
            '-----------\n'))
#------------------------------
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')
sleep(1)
#------------------------------
pedra = 1
papel = 2
tesoura = 3
lista = [1, 2, 3]
pc = random.choice(lista)
if eu == pedra and pc == tesoura:
    print('Você escolheu {} e o computador {} Empatou!!'.format(eu, pc))
elif eu == pedra and pc == papel:
    print('Você escolheu {} e o computador {} Você Perdeu!!'.format(eu, pc))
elif eu == pedra and pc == tesoura:
    print('Você escolheu {} e o computador {} Você Ganhou!!'.format(eu, pc))
elif eu == papel and pc == pedra:
    print('Você escolheu {} e o computador {} Você Ganhou!!'.format(eu, pc))
elif eu == papel and pc == papel:
    print('Você escolheu {} e o computador {} Empatou!!'.format(eu, pc))
elif eu == papel and pc == tesoura:
    print('Você escolheu {} e o computador {} Você Perdeu!!'.format(eu, pc))
elif eu == tesoura and pc == pedra:
    print('Você escolheu {} e o computador {} Você Perdeu!!'.format(eu, pc))
elif eu == tesoura and pc == papel:
    print('Você escolheu {} e o computador {} Você Ganhou!!'.format(eu, pc))
else:
    if eu == tesoura and pc == tesoura:
        print('Você escolheu {} e o computador {} Empatou!!'.format(eu, pc))