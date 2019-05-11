#coding: utf-8

area = float(raw_input('Área construída? '))
aliquota = float(raw_input('Aliquota? '))

iptu = (area * aliquota) + 35

#pagamento
quota_unica = iptu * 0.75

em_6_parcelas = iptu * 0.95
valor_6_parcelas = em_6_parcelas / 6

em_10_parcelas = iptu * 1.0
valor_10_parcelas = iptu / 10
print 'IPTU: R$ %.2f' % iptu
print 
print 'Pagamento:'
print '1. Quota única. R$ %.2f' % quota_unica
print '2. Em 6 parcelas. Total: R$ %.2f' % em_6_parcelas
print    '6 x R$ %.2f' % valor_6_parcelas
print '3. Em 10 parcelas. Total: R$ %.2f' % em_10_parcelas
print    '10 x R$ %.2f' % valor_10_parcelas
