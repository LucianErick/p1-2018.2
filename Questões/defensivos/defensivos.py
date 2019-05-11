#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Defensivos

tipo_de_produto = raw_input()
area_hectares = float(raw_input())
fungicida =  (1.0 * area_hectares / 50.0)
herbicida =  (0.3 * area_hectares / 1.0)
inseticida = (2.5 * area_hectares / 30.0)

#Calcular quantidade:

if   tipo_de_produto == 'Fungicida' and fungicida % 1 == 0:
     quantidade = int(fungicida)
     
elif tipo_de_produto == 'Fungicida' and fungicida % 1 != 0: 
     quantidade = int(fungicida) + 1	    
     
elif tipo_de_produto == 'Herbicida' and herbicida % 1 == 0: 
	 quantidade = int(herbicida)
	 
elif tipo_de_produto == 'Herbicida' and herbicida % 1 != 0:
	 quantidade = int(herbicida) + 1

elif tipo_de_produto == 'Inseticida' and inseticida % 1 == 0:
	 quantidade = int(inseticida) 

elif tipo_de_produto == 'Inseticida' and inseticida % 1 != 0: 	  	  	
	 quantidade = int(inseticida) + 1
	 

#Calcular preço :

if   tipo_de_produto == 'Fungicida':
	 preco = quantidade * 320.0
	 
elif tipo_de_produto == 'Herbicida':
	 preco = quantidade * 100.0

elif tipo_de_produto == 'Inseticida':
	 preco = quantidade * 400.0
	 
print '%d %s(s). %.2f reais.' % (quantidade, tipo_de_produto, preco)
	 	 	   

	 
