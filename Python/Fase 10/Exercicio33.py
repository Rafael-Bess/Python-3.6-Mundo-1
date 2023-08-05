print ('\033[1;34;30mVamos analisar entre três números inteiros qual é o maior e qual é o menor?\033[m')
n1 = int(input('\033[1;34;30mDigite o primeiro número:\033[m'))
n2 = int(input('\033[1;34;30mDigite o segundo número:\033[m'))
n3 = int(input('\033[1;34;30mDigite o terceiro número:\033[m'))
lista = [n1, n2, n3]
Organizados = sorted(lista, reverse=True)
print(Organizados)