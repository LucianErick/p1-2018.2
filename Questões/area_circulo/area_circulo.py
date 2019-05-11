# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Área do Círculo

dia =  raw_input("Dia da semana? ")
orcamento =  int(raw_input("Orcamento? R$ "))
adultos =  int(raw_input("Numero de adultos? "))
criancas =  int(raw_input("Numero de criancas? "))
pizza = int(raw_input("Preco da pizza? R$ "))
refrigerante = float(raw_input("Preco do refrigerante? R$ "))
estacionamento = float(raw_input("Preco do estacionamento? R$ "))
cinema = float(raw_input("Preco do ingresso do cinema? R$ "))

gastos_alimentacao = pizza + refrigerante
gastos_cinema = (cinema + 2) * adultos + (cinema + 2 / 2) * criancas
gastos_total = gastos_cinema + gastos_alimentacao + estacionamento

print "========== Despesas de " + dia + " =========="
print "Despesas com alimentacao: R$ " + str(gastos_alimentacao)
print "Despesas com cinema: R$" + str(gastos_cinema)
print "Despesas por pessoa: R$" + str(gastos_total / criancas + adultos)
print "Saldo disponivel: " + str(orcamento - gastos_total)
