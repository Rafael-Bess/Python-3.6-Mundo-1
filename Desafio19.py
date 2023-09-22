from random import choices
nome1 = str(input('\033[4;31;40mNome Aluno 1:\033[m '))
nome2 = str(input('\033[4;31;40mNome Aluno 2:\033[m '))
nome3 = str(input('\033[4;31;40mNome Aluno 3:\033[m '))
nome4 = str(input('\033[4;31;40mNome Aluno 4:\033[m '))
lista = [nome1, nome2, nome3, nome4]
resultado = choices(lista)
print('\033[4;31;40mO Aluno escolhido foi {}\033[m'.format(resultado))


#print('O Aluno escolhido é {}'.format(random.choices(resultado)))
#anteriormente a primeira versão utilizei o print da seguinte forma, sem declarar o resutaldo c  omo variavel porém com o código acima caso eu precise depois da varias eu posso utiliza-la

# uma lista para o python fica SEMPRE ENTRE []
