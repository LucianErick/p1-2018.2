#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Gratificacao natalina

codigo = int(raw_input())

if codigo == 1:
   salario = 25000.0
   print 'Deverá receber em dezembro R$ %.2f.' % salario 
   
if codigo == 2:
   salario = 15000.0
   print 'Deverá receber em dezembro R$ %.2f.' % salario 

faltas = int(raw_input())

if codigo == 3 and faltas == 0:
   gratificacao =  500.0
   salario = 8000.0 + gratificacao   
   print 'Valor da gratificação R$ %.2f.' % gratificacao 
   print 'Deverá receber em dezembro R$ %.2f.' % salario
 
if codigo == 3 and faltas > 0:
   gratificacao = (235 - faltas) * 2.0
   salario = 8000.0 + gratificacao
   print 'Valor da gratificação R$ %.2f.' % gratificacao 
   print 'Deverá receber em dezembro R$ %.2f.' % salario
   
if codigo == 4 and faltas == 0:
   gratificacao = 300.0
   salario = 5000.0 + gratificacao
   print 'Valor da gratificação R$ %.2f.' % gratificacao 
   print 'Deverá receber em dezembro R$ %.2f.' % salario

if codigo == 4 and faltas > 0:
   gratificacao = (235 - faltas) * 1.0
   salario = 5000.0 + gratificacao
   print 'Valor da gratificação R$ %.2f.' % gratificacao 
   print 'Deverá receber em dezembro R$ %.2f.' % salario

if codigo == 5 and faltas == 0:
   gratificacao = 200.0
   salario = 2800.0 + gratificacao
   print 'Valor da gratificação R$ %.2f.' % gratificacao 
   print 'Deverá receber em dezembro R$ %.2f.' % salario	

if codigo == 5 and faltas > 0:
   gratificacao = (235 - faltas) * 0.70
   salario = 2800.0 + gratificacao 
   print 'Valor da gratificação R$ %.2f.' % gratificacao 
   print 'Deverá receber em dezembro R$ %.2f.' % salario    
    	
