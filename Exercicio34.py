Salario = float(input('\033[1;34;30mInsira seu salario R$:\033[m'))
Calculo1 = Salario * 10 / 100
Calculo2 = Salario * 15 / 100
if Salario >= 1250.00:
    (print('\033[1;34;30mSeu aumento será de: {}\033[m'.format(Calculo1)))
else:
    (print('\033[1;34;30mSeu Aumento será de: {}\033[m'.format(Calculo2)))
