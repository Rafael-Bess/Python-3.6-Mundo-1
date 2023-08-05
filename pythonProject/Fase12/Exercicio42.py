'''
Refaça o DESAFIO 035 dos triângulos, e acrescentando o recusrdo de mostrar que tipo de triângulo será formado:

Equilátero: Todos os lados iguais
Isósceles: Dois lados iguais
Escaleno: todos os lados diferentes
'''

Base = int(input('\033[4;31;40mInsira o tamanho da base:\033[m'))
Extremidade1 = int(input('\033[4;31;40mInsira o tamanho da esquerda:\033[m'))
Extremidade2 = int(input('\033[4;31;40mInsira o tamanho da direita:\033[m'))
if Base < Extremidade1 + Extremidade2:
    (print('\033[4;33;40mÉ possivel montar um triangulo\033[m'))
else:
    (print('\033[4;33;40mNão é possivel montar um triangulo\033[m'))
if Base == Extremidade1 and Base == Extremidade2:
    print('\033[4;31;40mEsse triangulo é um Equilátero\033[m')
elif (Base == Extremidade1) or (Base == Extremidade2) or (Extremidade1 == Extremidade2):
    print('Esse Triangulo é um Isósceles')
else:
  if Base != Extremidade1 and Base != Extremidade2:
    print('Esse Triangulo é um Escaleno')
