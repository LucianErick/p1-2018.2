#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Embarque passageiros

primeira_classe = int(raw_input())
classe_economica = int(raw_input())
primeira_outro_voo = 0 
economica_primeira = 0 
economica_outro_voo = 0 


if (primeira_classe - 10) <= 0:
   primeira_outro_voo = 0

if (primeira_classe - 10) > 0:
   primeira_outro_voo = primeira_classe - 10

if (classe_economica - 100) <= 0: 
   economica_primeira = 0      	

if (classe_economica - 100) > 0 and (10 - primeira_classe) > 0:
   economica_primeira = (10 - primeira_classe)     

if (classe_economica - 100) > 0 and (10 - primeira_classe) <= 0:
   economica_primeira = 0

if (classe_economica - 100) > 0 and ((10 - primeira_classe) + (classe_economica - 100)) > 0:
   economica_outro_voo =  (classe_economica - 100) - (10 - primeira_classe)  


passageiros = (primeira_classe + classe_economica) - (primeira_outro_voo + economica_outro_voo) 
 
print '%s passageiro(s) da primeira classe remanejado(s) para outro voo.' % primeira_outro_voo  
print '%s passageiro(s) da econômica remanejado(s) para a primeira classe.' % economica_primeira
print '%s passageiro(s) da econômica remanejado(s) para outro voo.' % economica_outro_voo 
print '%s passageiros embarcados.' % passageiros

