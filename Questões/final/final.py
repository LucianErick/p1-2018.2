#coding: utf-8

#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#UFCG - Programação 1
print '== Estágio 1 =='
peso1 = float(raw_input('Peso? '))
nota1 = float(raw_input('Nota? '))
print '== Estágio 2 =='
peso2 = float(raw_input('Peso? '))
nota2 = float(raw_input('Nota? '))
print '== Estágio 3 =='
peso3 = float(raw_input('Peso? '))
nota3 = float(raw_input('Nota? '))

media_parcial = peso1 * nota1 + peso2 * nota2 + peso3 * nota3
nota_final_5 = abs((media_parcial * 0.6) - 5.0) / 0.4   
nota_final_maior_que_7 = abs((media_parcial * 0.6) - 7.0) / 0.4

print '== Resultados =='
print 'Média parcial: %.1f' % media_parcial
print 'Nota na final, pra média 5.0 = %.1f' % nota_final_5 
print 'Nota na final, pra média 7.0 = %.1f' % nota_final_maior_que_7
