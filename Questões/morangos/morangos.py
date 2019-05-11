#coding: utf-8

#ALuno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#UFCG - Programação 1

morangos = int(raw_input())
caixas_necessarias = morangos / 400
sobras = (float((morangos - caixas_necessarias * 400)) / morangos) * 100  


print 'Serão necessárias %i caixa(s) para embalar os morangos.' % caixas_necessarias  
print '%.1f' % sobras + '% dos morangos serão perdidos.'
