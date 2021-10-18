def Gemiddelde( lijst ):
    aantalc=0
    totaal=0
    for cijfer in lijst:
        totaal += cijfer
        aantalc += 1
    G = totaal / aantalc
    return G

lijst = [ 14, 5, 8, 9, 13, 18, 16, 25 ]
G = Gemiddelde( lijst )
print( G )

