# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Espaço em disco simplificado

login1 = raw_input()
espaco1 = int(raw_input())

login2 = raw_input()
espaco2 = int(raw_input())

login3 = raw_input()
espaco3 = int(raw_input())
 
print 'SPLab - Espaço utilizado pelos usuários'
print '---------------------------------------------'
print 'Nr., Usuário, Espaço Utilizado'

conversao1 = (espaco1 * 1.0 / 1024) / 1024
conversao2 = (espaco2 * 1.0 / 1024) / 1024
conversao3 = (espaco3 * 1.0 / 1024) / 1024

print '1, %s, %.2f MB' % (login1, conversao1)
print '2, %s, %.2f MB' % (login2, conversao2)
print '3, %s, %.2f MB' % (login3, conversao3)

total = conversao1 + conversao2 + conversao3
media = total / 3

print 'Espaço total ocupado: %.2f MB' % total 
print 'Espaço médio ocupado: %.2f MB' % media
