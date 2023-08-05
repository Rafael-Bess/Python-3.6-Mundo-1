#faz um programa ler preço de produto calcular mostrar o preço com desconto a vista 10% e com aumento para parcelado aumento de %8
prod = float(input('\033[7;31;40mQual o valor do seu produto?\033[m'))
desc = float(10/100 * prod)
ndes = float(prod - desc)
aume = float(8/100 * prod)
naum = float(prod + aume)
print('\033[7;31;40mO valor do seu produto é R$:{:.2f} com desconto de 10% fica R$:{:.2f}\033[m'.format(prod, ndes))
print('\033[7;31;40mO valor do seu produto é R$:{:.2f} com aumento de 8% fica R$:{:.2f}\033[m'.format(prod, naum))
