# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Campos de futebol

area_1 = float(raw_input())
area_2 = float(raw_input())
area_3 = float(raw_input())

campos_1 = area_1 / 4000
campos_2 = area_2 / 4000
campos_3 = area_3 / 4000

media = (campos_1 + campos_2 + campos_3) / 3 

print '%.2f' % campos_1
print '%.2f' % campos_2
print '%.2f' % campos_3
print '%.2f' % media
