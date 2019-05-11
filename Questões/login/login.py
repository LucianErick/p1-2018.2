#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Verifica Login

email = str(raw_input())
senha = str(raw_input())

admin_email = 'admin@tst.ufcg.edu.br'
senha_admin = 'TstAdminProg1'

if email == admin_email and senha == senha_admin:
    print 'Login efetuado com sucesso!'
elif email == admin_email and not senha == senha_admin:
    print 'Senha inválida. Tente novamente.'
elif not email == admin_email and senha == senha_admin:
    print 'Email inválido.'
elif not email == admin_email and not senha == senha_admin:
    print 'Login inválido.'         	
