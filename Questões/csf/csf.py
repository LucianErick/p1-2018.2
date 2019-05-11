#coding: utf-8
#Aluno: Ana Carolina Chaves de Vasconcelos

#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Ciência sem fronteiras

nota_enem = float(raw_input())
creditos = int(raw_input())

condicao_creditos = 374.4 >= creditos >= 83.2

condicao_enem = nota_enem >= 600

if not condicao_enem and condicao_creditos:
   
   condicao = 'Condição ENEM não satisfeita.'
   print condicao

elif condicao_enem and not condicao_creditos:
   condicao = 'Condição CRÉDITOS não satisfeita.'
   print condicao

elif not condicao_enem and not condicao_creditos:
   condicao = 'Nenhuma condição satisfeita.'
   print condicao	     

elif condicao_enem and condicao_creditos:
   condicao = 'Todas as condições satisfeitas.'
   print condicao
