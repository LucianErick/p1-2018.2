#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Classifica Corredor

distancia = float(raw_input()) 
tempo = float(raw_input())

velocidade = distancia / tempo

if velocidade < 10:
    tipo_de_corredor = 'Corredor amador.'
    print 'Velocidade: %.1fkm/h. %s' % (velocidade, tipo_de_corredor)
   
elif 15 >= velocidade >= 10: 
    tipo_de_corredor = 'Corredor aspirante.'
    print 'Velocidade: %.1fkm/h. %s' % (velocidade, tipo_de_corredor)
    
elif velocidade > 15: 
    tipo_de_corredor = 'Corredor profissional.'
    print 'Velocidade: %.1fkm/h. %s' % (velocidade, tipo_de_corredor)
  
    
