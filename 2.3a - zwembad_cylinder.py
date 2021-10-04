import math

# deze functie berekent de oppervlakte van een cirkel
def fOppervlakte( straal ):
    opp = straal ** 2 * math.pi
    return opp

# deze functie berekent de inhoud van een zwembad
def fBerekenInhoudCylinder( hoogte, diameter ):
    mijn_oppervlakte = fOppervlakte( diameter / 2 ) # oppervlakte laten uitrekenen door de functie fOppervlakte
    volume = int( mijn_oppervlakte * hoogte * 1000) # volume berekenen
    print("De inhoud van het zwembad is %s liter" % volume )

fBerekenInhoudCylinder( hoogte = 0.5, diameter = 3 )
fBerekenInhoudCylinder( hoogte = 0.6, diameter = 4 )
fBerekenInhoudCylinder( hoogte = 0.8, diameter = 5.5 ) # benoemde argumenten maken de code duidelijker