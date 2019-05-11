# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.1
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Acima do limite

limite = int(raw_input())
soma = 0

while True:
	caracteres = raw_input()
	lista = caracteres.split(' ')
	if caracteres == '-':
	   break
	for i in range(len(lista)):
      
		soma += int(lista[i])
        
        if soma > 5 * limite:
	       break
    	
	
	    
		
	  	   
print soma

    
