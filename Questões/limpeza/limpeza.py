#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Limpeza

servico = int(raw_input())

if servico == 3: 
	valor =  50.0
	print 'R$ %d,00' % valor
    
elif servico == 1 or servico == 2:
   
	tamanho = int(raw_input())	   
 
	if servico == 1:
		preco = 80 * tamanho    
	
		if servico == 1 and preco >= 200:
			print 'R$ %d,00' % preco  
			print 'Brinde!'
	
		elif servico == 1 and preco < 200:
			print 'R$ %d,00' % preco
	
	elif servico == 2:
		preco = 50 * tamanho

		if servico == 2 and preco >= 200:
			print 'R$ %d,00' % preco
			print 'Brinde!'
		
		elif servico == 2 and preco < 200:
			print 'R$ %d,00' % preco       

