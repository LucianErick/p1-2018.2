#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Resumo das vendas

vendas_da_loja = int(raw_input())
vendas_por_teresa = int(raw_input())
vendas_por_carla = int(raw_input())
vendas_por_joaquim = int(vendas_da_loja - (vendas_por_carla + vendas_por_teresa))
percentual_carla = (vendas_por_carla * 1.0 / vendas_da_loja) * 100
percentual_teresa = (vendas_por_teresa * 1.0 / vendas_da_loja) * 100.0
percentual_joaquim = (vendas_por_joaquim * 1.0 / vendas_da_loja) * 100.0

print 'Teresa vendeu %d (de %d) brinquedos. (%.2f%%)' % (vendas_por_teresa, vendas_da_loja,percentual_teresa)
print 'Joaquim vendeu %d (de %d) brinquedos. (%.2f%%)' % (vendas_por_joaquim, vendas_da_loja,percentual_joaquim)
print 'Carla vendeu %d (de %d) brinquedos. (%.2f%%)' % (vendas_por_carla,vendas_da_loja,percentual_carla)

