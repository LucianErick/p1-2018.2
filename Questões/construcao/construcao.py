#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Orçamento construção

preco_tijolo = float(raw_input('Digite o preço da unidade do tijolo (Em reais): '))
altura_tijolo = float(raw_input('Digite a altura do tijolo (Em metros): '))
comprimento_tijolo = float(raw_input('Digite o comprimento do tijolo (Em metros): '))
altura_parede = float(raw_input('Digite a altura das paredes (Em metros): '))
comprimento_parede = float(raw_input('Digite o comprimento das paredes (Em metros): '))

num_tijolos_altura = altura_parede / altura_tijolo 
num_tijolos_largura =  comprimento_parede / comprimento_tijolo
num_tijolos_total = num_tijolos_altura * num_tijolos_largura
orcamento_tijolos = num_tijolos_total * preco_tijolo
print 'O número total de tijolos é %.1f e o orçamento final é de R$ %.1f' % (num_tijolos_total, orcamento_tijolos)
