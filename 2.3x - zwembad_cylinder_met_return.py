import math     # wiskundige functies, o.a. pi

def oppervlakte( straal ):
    # uitkomst terug doorgeven voor verder gebruik
    return straal * straal * math.pi

def inhoud( hoogte, straal ):
    straal = straal / 2
    opp = oppervlakte(straal)
    # uitkomst terug doorgeven voor verder gebruik
    return round( hoogte * opp , 2  )

print("De inhoud van zwembad1 is %s liter" % inhoud( 0.5, 3 ) )
print("De inhoud van zwembad2 is %s liter" % inhoud( 0.6, 4 ) )
print("De inhoud van zwembad3 is %s liter" % inhoud( 0.8, 5.5 ) )
