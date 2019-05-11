# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I | 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Caixa Preta (Descartando Leituras)

n_p = 0
n_c = 0
n_a = 0


while True:

    dados = raw_input().split()

    peso = dados[0]
    combustivel = dados[1]
    altitude = dados[2]

    if int(peso) < 0:

       print 'dado inconsistente. peso negativo.'

       break

    else:

        n_p += 1


    if int(combustivel) < 0:

       print 'dado inconsistente. combustível negativo.'
       break

    else:

        n_c += 1

    if int(altitude) < 0:

       print 'dado inconsistente. altitude negativa.'

       break

    else:

        n_a += 1

print 'peso: %d' % (n_p)
print 'combustível: %d' % (n_c)
print 'altitude: %d' % (n_a)
