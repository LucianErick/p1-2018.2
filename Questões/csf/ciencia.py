#coding: utf-8
#Ana Carolina Chaves
#Programação 1
#118110388

nota_enem = float(raw_input())
creditos = int(raw_input())

condicao_creditos = 374.4 >= creditos >= 83.2
condicao_enem = nota_enem >= 600.0

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
