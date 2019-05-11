ano = 365
mes = 30

dias = int(raw_input())

anos = dias / ano
sobra_anos = dias % ano

meses = sobra_anos / mes
sobra_meses = sobra_anos % mes

dia = dias - meses * 30 + anos * 365 

if dia > 30:
   meses = meses + (dia / 30)

if meses > 12:
   anos = anos + (meses / 12)   	

print '%d ano(s)' % anos
print '%d mes(es)' % meses
print '%d dia(s)' % dia
