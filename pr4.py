from fractions import Fraction
a=int(input('Dati numaratorul primei fractii (a)= '))
b=int(input('Dati numitorul primei fractii (b)= '))
c=int(input('Dati numaratorul celei de a doua fractii (c)= '))
d=int(input('Dati numitorul celei de a doua fractii (d)= '))
print('Suma fractiilor este = ',Fraction(a,b)+Fraction(c,d))
print('Produsul fractiilor este = ',Fraction(a,b)*Fraction(c,d))