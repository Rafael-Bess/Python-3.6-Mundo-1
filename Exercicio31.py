Distancia = float(input('\033[4;31;40mDigite a distancia da viagem:\033[m'))
print ('\033[4;31;40mSua viagem será de {} Km.\033[m')
Passagem = Distancia * 0.50
Passagem2 = Distancia * 0.45
if Distancia <= 200:
    (print('\033[4;31;40mO valor da sua passagem será de {} e você percorreu {} KMD)\033[m'.format(Passagem, Distancia)))
else:
    (print('\033[4;31;40mO valor da sua passagem será de {} e você percorreu {} KM\033[m'.format(Passagem2, Distancia)))
