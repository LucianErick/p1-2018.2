#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: unidades e medidas

medida = float(raw_input('Medida em metros? '))

medida_em_centimetros = medida * 100
um_cm_para_polegadas = 0.3937007874015748
um_cm_para_pes = 0.03280839895013123
um_cm_para_jardas = 0.010936132983377079

polegadas = medida_em_centimetros * um_cm_para_polegadas
pes = medida_em_centimetros * um_cm_para_pes
jardas = medida_em_centimetros * um_cm_para_jardas 

print 'Jardas: %.3f yd' % jardas 
print 'Pés: %.3f ft' % pes
print 'Polegadas: %.3f in' % polegadas
 
