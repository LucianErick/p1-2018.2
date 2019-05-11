#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Densidade

massa_1 = float(raw_input())
volume_1 = float(raw_input())
massa_2 = float(raw_input())
volume_2 = float(raw_input())
massa_3 = float(raw_input())
volume_3 = float(raw_input())

densidade_1 = massa_1 / volume_1
densidade_2 = massa_2 / volume_2
densidade_3 = massa_3 / volume_3

if   densidade_3 > densidade_1 and densidade_2 > densidade_1:    
     print 'O líquido 1, com densidade %.2f, irá ocupar a parte de cima do recipiente.' % densidade_1

elif densidade_1 > densidade_2 and densidade_3 > densidade_2:
     print 'O líquido 2, com densidade %.2f, irá ocupar a parte de cima do recipiente.' % densidade_2
 
elif  densidade_1 > densidade_3 and densidade_2 > densidade_3:
     print 'O líquido 3, com densidade %.2f, irá ocupar a parte de cima do recipiente.' % densidade_3


