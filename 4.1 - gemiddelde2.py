def Gemiddelde( lijst ):
    aantalc=len(lijst)
    totaal=sum(lijst)
    G = totaal / aantalc
    return G

lijst = [ 14, 5, 8, 9, 13, 18, 16, 25 ]
G = Gemiddelde( lijst )
print( G )

