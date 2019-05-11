#coding: utf-8

#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#UFCG - Progamação 1

capacidade = float(raw_input('capacidade? '))
percentual = float(raw_input('percentual hoje? '))
consumo = float(raw_input('gasto diário? '))

volume_disponivel = capacidade * (percentual/100)
dias_restantes = int(volume_disponivel / consumo)

print 'volume: %.2f' % volume_disponivel
print 'dias restantes: %i' % dias_restantes 
