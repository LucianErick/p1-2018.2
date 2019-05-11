# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Imprime Nota Fiscal

valor_total = float(raw_input())
data = raw_input()
quantidade_de_produtos = int(raw_input())

media = valor_total / quantidade_de_produtos

print 'Data: %s' % data
print 'O valor total da compra foi de R$ %.2f. A média do preço dos produtos é de %.1f.' % (valor_total, media)


