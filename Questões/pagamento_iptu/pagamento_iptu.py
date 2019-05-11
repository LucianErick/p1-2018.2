#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: IPTU escolhendo forma de pagamento
 
area = float(raw_input())
metro_quadrado = float(raw_input())
pagamento = raw_input()

iptu = area * metro_quadrado 

desconto_a_vista = iptu * 0.8
desconto_2x = iptu * 0.9
parcela_2x = desconto_2x / 2
desconto_3x = iptu * 0.95
parcela_3x = desconto_3x / 3

if pagamento == 'vista':
   print 'Total: R$ %.2f' % desconto_a_vista	  

elif pagamento == '2x':
   print 'Total: R$ %.2f. Parcelas: R$ %.2f' % (desconto_2x, parcela_2x) 

elif pagamento == '3x':
   print 'Total: R$ %.2f. Parcelas: R$ %.2f' % (desconto_3x, parcela_3x) 
