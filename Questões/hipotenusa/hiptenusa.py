#coding: utf-8
#Aluno: luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#UFCG - Programação 1
import math
cateto1 = float(raw_input('Medida do Cateto 1? '))
cateto2 = float(raw_input('Medida do Cateto 2? '))
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

print 'Medida da Hipotenusa: %.2f' % hipotenusa 
