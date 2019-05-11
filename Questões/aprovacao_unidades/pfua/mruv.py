# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: MRUV

s0 = float(raw_input('Posição inicial? '))
v0 = float(raw_input('Velocidade inicial? '))
t = float(raw_input('Tempo? '))
a = float(raw_input('Aceleração? '))

v = v0 + (a * t)
s = s0 + (v0 * t) + (a * t ** 2 / 2)
vm = (s - s0) / t

print 
print 'Dados da questão'
print '================'
print '   Posição inicial: %.2f m' % s0
print 'Velocidade inicial: %.2f m/s' % v0 
print '        Aceleração: %.2f m/s2' % a
print '             Tempo: %.2f s' % t
print '  Velocidade final: %.2f m/s' % v
print '  Velocidade média: %.2f m/s' % vm
print '     Posição final: %.2f m' % s


