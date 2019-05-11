#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#UFCG - Programação 1

custo = float(raw_input())
despesas = float(raw_input())
lucro = float(raw_input())
impostos = float(raw_input())
comissoes = float(raw_input())
descontos = float(raw_input())
encargos = float(raw_input())

porcentagem_venda = (despesas + lucro) / 100.0
preco_venda = custo + (custo * porcentagem_venda)
preco_venda_1 = (100 / (100 - impostos - comissoes - descontos - encargos))
valor_total = preco_venda_1 * preco_venda
resto = valor_total % int(valor_total)

print "Preço de venda é R$ %.2f (R$ %.2f + R$ %.2f)" % (valor_total,int(valor_total),resto)
