#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Maior pequeno primo

numero = int(raw_input())

if numero / 7 and numero % 7 == 0:
   K = numero / 7
   print '7 * %d = %d' % (K, numero)

elif numero / 5 and numero % 5 == 0:
   K = numero / 5
   print '5 * %d = %d' % (K, numero)

elif numero / 3 and numero % 3 == 0:
   K = numero / 3
   print '3 * %d = %d' % (K, numero)
   
elif numero / 2 and numero % 2 == 0:
   K = numero / 2
   print '2 * %d = %d' % (K, numero)
      
else:
   print '%d não tem fatores primos menores que 10' % numero    
