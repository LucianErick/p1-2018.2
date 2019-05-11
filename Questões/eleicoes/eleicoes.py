#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Eleições

votos_a = int(raw_input())
votos_b = int(raw_input())
votos_c = int(raw_input())

total_votos = votos_a + votos_b + votos_c

percenta_votos_a = votos_a * 100.0 / total_votos
percenta_votos_b = votos_b * 100.0 / total_votos
percenta_votos_c = votos_c * 100.0 / total_votos 

if votos_a > votos_b and votos_a > votos_c and percenta_votos_a > 50.00:
    print'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato A, segundo turno = Não' % (percenta_votos_a, percenta_votos_b, percenta_votos_c)
    
elif votos_a > votos_b and votos_a > votos_c and percenta_votos_a <= 50.00:
    print'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato A, segundo turno = Sim' % (percenta_votos_a, percenta_votos_b, percenta_votos_c)
    
elif votos_b > votos_a and votos_b > votos_c and percenta_votos_b > 50.00:
    print'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato B, segundo turno = Não' % (percenta_votos_a, percenta_votos_b, percenta_votos_c)
    
elif votos_b > votos_a and votos_b > votos_c and percenta_votos_b <= 50.00:
    print'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato B, segundo turno = Sim' % (percenta_votos_a, percenta_votos_b, percenta_votos_c)        
    
elif votos_c > votos_b and votos_c > votos_a and percenta_votos_c > 50.00:
    print'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato C, segundo turno = Não' % (percenta_votos_a, percenta_votos_b, percenta_votos_c)
    
elif votos_c > votos_b and votos_c > votos_a and percenta_votos_c <= 50.00:
    print'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato C, segundo turno = Sim' % (percenta_votos_a, percenta_votos_b, percenta_votos_c)
