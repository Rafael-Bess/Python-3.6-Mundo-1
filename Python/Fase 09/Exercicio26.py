frase = str(input('\033[4;31;40mInsira sua frase:\033[m')).upper().strip()
print('\033[4;31;40mA letra A aparece {} na frase\033[m'.format(frase.count('A')))
print('\033[4;31;40mA letra A se iniciou em {}\033[m'.format(frase.find('A') + 1))
print('\033[4;31;40mA letra A possui a ultima posição {}\033[m'.format(frase.rfind('A') + 1))