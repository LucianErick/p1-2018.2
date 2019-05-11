# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Calcula preço de venda 

custo = float(raw_input())
despesas = float(raw_input())
lucro = float(raw_input())
impostos = float(raw_input())
comissoes = float(raw_input())
descontos = float(raw_input())
encargos = float(raw_input())

porcenta_venda = (despesas + lucro) / 100.0
preco_venda = custo + custo * porcenta_venda
preco_venda1 = (100 / (100 - impostos - comissoes - descontos - encargos))
valor_total = preco_venda1 * preco_venda
resto = valor_total % int(valor_total)

print "Preço de venda é R$ %.2f (R$ %.2f + R$ %.2f)" % (valor_total,int(valor_total),resto)
