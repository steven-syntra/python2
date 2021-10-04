import math     # wiskundige functies, o.a. pi

def InhoudKegel( hoogte, diameter1, diameter2 ):
    straal1 = diameter1 / 2 # de straal is de helft van de diameter
    straal2 = diameter2 / 2 # de straal is de helft van de diameter

    #het volume berekenen met de opgegeven formule
    volume = (1 / 3) * math.pi * hoogte * ( straal1**2 + straal1*straal2 + straal2**2 )

    # m³ omzetten naar liter
    aantal_liter = volume * 1000
    return aantal_liter


inhoud_k = InhoudKegel( 6, 8, 12)
print( "De kegel bevat %s liter" % int(inhoud_k) )

