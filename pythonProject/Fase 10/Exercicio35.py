Base = int(input('\033[4;31;40mInsira o tamanho da base:\033[m'))
Extremidade1 = int(input('\033[4;31;40mInsira o tamanho da esquerda:\033[m'))
Extremidade2 = int(input('\033[4;31;40mInsira o tamanho da direita:\033[m'))
if Base < Extremidade1 + Extremidade2:
    (print('\033[4;31;40mÉ possivel montar um triangulo\033[m'))
else:
    (print('\033[4;31;40mNão é possivel montar um triangulo\033[m'))