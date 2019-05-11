# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Nota na final

print '== Estágio 1 =='
peso1 = float(raw_input('Peso? '))
nota1 = float(raw_input('Nota? '))
print '== Estágio 2 =='
peso2 = float(raw_input('Peso? ')) 
nota2 = float(raw_input('Nota? '))
print '== Estágio 3 =='
peso3 = float(raw_input('Peso? '))
nota3 = float(raw_input('Nota? '))

parcial = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3) / (peso1 + peso2 + peso3)

nota_5 = ((parcial * 0.6 - 5.0) / 0.4) * - 1  

nota_7 = ((parcial * 0.6 - 7.0) / 0.4) * - 1

print '== Resultados =='
print 'Média parcial: %.1f' % parcial
print 'Nota na final, pra média 5.0 = %.1f' % nota_5
print 'Nota na final, pra média 7.0 = %.1f' % nota_7
     
