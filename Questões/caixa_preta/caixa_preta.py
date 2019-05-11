# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I | 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Caixa Preta


quantidade = int(raw_input())
medicoes = ''
# Quando garantia positivo for igual a 0, ele é um numero positivo, quando é 1, negativo 

garantia_positivo = 0
for m in range(quantidade):
	 medicoes = raw_input().split()
	 
	 peso = int(medicoes[0])
	 combustivel = int(medicoes[1])
	 altitude = int(medicoes[2])
	 
	 if garantia_positivo == 0:
		
		if peso < 0:
			print'dado inconsistente. peso negativo.'
				
		elif combustivel < 0:
			print'dado inconsistente. combustível negativo.'
		    
		elif altitude < 0:
			print'dado inconsistente. altitude negativa.'
		    
		    
	 if garantia_positivo == 0:
		 
		 
		 soma = 0
		 
		 for i in medicoes:
			 if int(i) >= 0:
				soma += 1
			 
	 else:
				 
		 garantia_positivo = 1
      
		 break 
		 
print'%i dados válidos.' % soma
