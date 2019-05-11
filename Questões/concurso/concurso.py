#coding: utf-8
#Aluna: Ana Carolina Chaves de Vasconcelos
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1 | 2018.2
#Problema: Concurso


nota_1 = float(raw_input())
nota_2 = float(raw_input())
nota_3 = float(raw_input())
idade_candidato_1 = int(raw_input())
nota_4 = float(raw_input())
nota_5 = float(raw_input())
nota_6 = float(raw_input())
idade_candidato_2 = int(raw_input())

media_candidato_1 = nota_1 * 0.3 + nota_2 * 0.4 + nota_3 * 0.3
media_candidato_2 = nota_4 * 0.3 + nota_5 * 0.4 + nota_6 * 0.3

if media_candidato_1 > media_candidato_2 or media_candidato_1 == media_candidato_2 and idade_candidato_1 > idade_candidato_2:
   resultado = 'O primeiro candidato foi aprovado com média %.1f.' % media_candidato_1
   print resultado
elif media_candidato_2 > media_candidato_1 or media_candidato_2 == media_candidato_1 and idade_candidato_2 > idade_candidato_1:
   resultado = 'O segundo candidato foi aprovado com média %.1f.' % media_candidato_2
   print resultado
elif media_candidato_1 == media_candidato_2 and idade_candidato_1 == idade_candidato_2:
   resultado = 'Empate.' 
   print resultado
