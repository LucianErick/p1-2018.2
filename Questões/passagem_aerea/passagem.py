# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Passagem aérea

distancia = float(raw_input())
aliquota = float(raw_input())
taxa_fixa = 51.0

valor_passagem = distancia * aliquota + taxa_fixa

valor_a_vista = 0.75 * valor_passagem
valor_em_6_vezes = 0.95 * valor_passagem
valor_em_10_vezes = 1.0 * valor_passagem

parcelas_6_vezes = valor_em_6_vezes * 1.0 / 6
parcelas_10_vezes = valor_em_10_vezes * 1.0 / 10

print 'Valor da passagem: R$ %.2f' % valor_passagem
print
print 'Pagamento:'
print '1. À vista. R$ %.2f' % valor_a_vista
print '2. Em 6 parcelas. Total: R$ %.2f' % valor_em_6_vezes
print '   6 x R$ %.2f' % parcelas_6_vezes
print '3. Em 10 parcelas. Total: R$ %.2f' % valor_em_10_vezes 
print '   10 x R$ %.2f' % parcelas_10_vezes
