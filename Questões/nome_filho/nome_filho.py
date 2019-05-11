#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Escolhendo o nome do filho

pai = raw_input()
avo_paterno = raw_input()
avo_materno = raw_input()

if (pai != avo_paterno) and (pai != avo_materno) and (avo_materno != avo_paterno):
   nome = '%s %s %s' % (pai, avo_paterno, avo_materno)
   print nome
   
elif pai == avo_paterno and pai != avo_materno and avo_paterno != avo_materno:
   print avo_materno

elif pai == avo_materno and pai != avo_paterno and avo_paterno != avo_materno:
   print avo_paterno
      
elif avo_materno == avo_paterno and avo_materno != pai and avo_materno != pai:
   print pai
             
elif pai == avo_materno == avo_paterno:
   print 'Rafael'
   	             
