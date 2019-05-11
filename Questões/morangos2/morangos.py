# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Caixas com Morangos 

morangos = int(raw_input())

caixas = morangos / 400

resto = morangos % 400

perdidos = resto * 100.0 / morangos

print 'Serão necessárias %i caixa(s) para embalar os morangos.' % caixas
print '%.1f%% dos morangos serão perdidos.' % perdidos
 
