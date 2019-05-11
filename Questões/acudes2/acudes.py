# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Açudes

capacidade = int(raw_input('capacidade? ')) 
percentual = float(raw_input('percentual hoje? ')) * 0.01
gasto = int(raw_input('gasto diário? '))

restante = capacidade * percentual

dias_restantes = int(restante / gasto)

print 'volume: %.2f' % restante
print 'dias restantes: %i' % dias_restantes

