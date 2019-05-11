# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Hipotenusa

import math

cateto1 = float(raw_input('Medida do Cateto 1? '))
cateto2 = float(raw_input('Medida do Cateto 2? '))

hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

print 'Medida da Hipotenusa: %.2f' % hipotenusa

