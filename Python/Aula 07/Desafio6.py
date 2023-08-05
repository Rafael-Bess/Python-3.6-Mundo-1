n = int(input('\033[4;30;45mDigite um número:\033[m '))
d = (n*2)
t = (n*3)
r = (n**(1/2))
print('Dobro é \033[4;30;45m{}\033[m o triplo é \033[4;30;45m{}\033[m e a raiz quadrada é \033[4;30;45m{:.2f}\033[m'.format(d,t,r))
# o porque do :.2f está no discord porém da pra perguntar pro GPT