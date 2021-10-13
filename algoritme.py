import math

math.gcd()


# input getal 1
g1 = int(input('Mag ik getal 1?'))
#input getal 2
g2 = int(input('En nu getal 2 aub...'))
#opslaan getallen voor print functie
getal1 = g1
getal2 = g2
# zolang  g2 groter is dan 0 zal de deling blijven doorgaan
while g2 > 0:
    # g1 wordt gedeeld door g2 en de waarde van g1 en g2 wordt omgekeerd,
    # dit zolang g2 groter dan 0 is
    g1, g2 = g2, g1 % g2
    print('g1=',g1,"g2=", g2)

print('De grootste gemene deler van',getal1, 'en', getal2, 'is', g1)



