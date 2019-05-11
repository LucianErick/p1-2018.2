#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Compatibilidade Sanguínea

abo_paciente = raw_input()
rh_paciente = raw_input()
abo_doador = raw_input()
rh_doador = raw_input()

if abo_paciente == 'O' and rh_paciente == '+' and abo_doador == 'O' and (rh_doador == '+' or rh_doador == '-') \
  or abo_paciente == 'O' and rh_paciente == '-' and abo_doador == 'O' and rh_doador == '-' \
  or abo_paciente == 'A' and rh_paciente == '+' and (abo_doador == 'O' or abo_doador == 'A') and (rh_doador == '+' or rh_doador == '-') \
  or abo_paciente == 'A' and rh_paciente == '-' and (abo_doador == 'O' or abo_doador == 'A') and rh_doador == '-' \
  or abo_paciente == 'B' and rh_paciente == '+' and (abo_doador == 'O' or abo_doador == 'B') and (rh_doador == '+' or rh_doador == '-') \
  or abo_paciente == 'B' and rh_paciente == '-' and (abo_doador == 'O' or abo_doador == 'B') and rh_doador == '-' \
  or abo_paciente == 'AB' and rh_paciente == '+' and (abo_doador == 'A' or abo_doador == 'B' or abo_doador == 'AB' or abo_doador == 'O') and (rh_doador == '+' or rh_doador == '-') \
  or abo_paciente == 'AB' and rh_paciente == '-' and (abo_doador == 'A' or abo_doador == 'B' or abo_doador == 'AB' or abo_doador == 'O') and rh_doador == '-':
  print 'compatível'

else:    
  print 'incompatível'
