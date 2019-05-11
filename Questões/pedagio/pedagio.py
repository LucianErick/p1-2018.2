#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Pedágio

veiculo = raw_input()

if veiculo == 'Motocicleta':
   valor = 5.70
   print 'Valor a pagar: R$ %.2f.' % (valor)
   
elif veiculo == 'Automóvel utilitário':
   valor = 11.40
   print 'Valor a pagar: R$ %.2f.' % (valor)
   
elif veiculo == 'Ônibus' or veiculo == 'Caminhão':
   eixos = int(raw_input())
   if veiculo == 'Ônibus':
      valor = 11.40 * eixos
      print 'Valor a pagar: R$ %.2f.' % (valor)
   elif veiculo == 'Caminhão':
      valor = 9.60 * eixos
      print 'Valor a pagar: R$ %.2f.' % (valor)  
      
else:
	print 'Veículo não cadastrado.'             
