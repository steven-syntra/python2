def Euclides(g1, g2):
    """ Deze functie berekent de grootste gemene
        deler van 2 opgegeven getallen g1 en g2
    """
    while g1 != g2:
        if g1 > g2:
            g1 -= g2    # g1 = g1 - g2
        else:
            g2 -= g1    # g2 = g2 - g1

    return g1

input1 = int( input("Geef een getal aub: ") )
input2 = int( input("Geef nog een getal aub: ") )
ggd = Euclides(input1, input2)
print("De grootste gemene deler van %s en %s is %s" % (input1, input2, ggd))