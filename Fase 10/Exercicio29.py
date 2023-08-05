from time import sleep
velocidade = int(input('\033[4;31;30mO carro passou a quantos km?\033[m'))
print('\033[4;31;30mProcessando...\033[m')
sleep(3)
multa = (velocidade - 80) * 30
if velocidade > 80:
    print('\033[4;31;30mOVocê foi multado por excesso de velocidade: {}\033[\n\033[4;31;30mO valor da multa é de {}R$\033[m'.format(velocidade, multa))
else:
    print('\033[4;31;30mOTenha um bom dia!! Dirija com cuidado\033[m')
