cidade = str(input('\033[1;30;44mDigite o nome de sua cidade: \033[m')).strip()
print('\033[1;30;44mA sua cidade é: {} e é {} para inicio Santo\033[m'.format(cidade.title(), 'SANTO' in cidade[:5].upper()))
