# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Vendas

loja = int(raw_input())
teresa = int(raw_input()) 
carla = int(raw_input())

joaquim = loja - (teresa + carla)

perc_teresa = (teresa * 100.0) / loja 
perc_joaquim = (joaquim * 100.0) / loja
perc_carla = (carla * 100.0) / loja

print 'Teresa vendeu %i (de %i) brinquedos. (%.2f%%)' % (teresa, loja, perc_teresa)
print 'Joaquim vendeu %i (de %i) brinquedos. (%.2f%%)' % (joaquim, loja, perc_joaquim)
print 'Carla vendeu %i (de %i) brinquedos. (%.2f%%)' % (carla, loja, perc_carla)
