from random import shuffle
n1 = str(input('\033[0;31;40mPrimeiro aluno:\033[m'))
n2 = str(input('\033[0;31;40mSegundo aluno:\033[m'))
n3 = str(input('\033[0;31;40mTerceiro aluno:\033[m '))
n4 = str(input('\033[0;31;40mQuarto aluno:\033[m '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('\033[0;31;40mOs Alunos escolhidos em ordem são {}\033[m'.format(lista))
#não precisei usar o random.shuffle porque eu importei apenas o shuffle

