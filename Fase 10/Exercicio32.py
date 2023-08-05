Ano = int(input('\033[4;35;40mInsira o ano atual:\033[m'))
Calculo = Ano % 4 == 0
if Calculo:
    (print('\033[4;35;40mSeu ano é bissexto:\033[m'))
else:
    (print('\033[4;35;40mSeu ano não é bissexto\033[m'))

