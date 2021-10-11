kapitaal = int( input("Wat is het kapitaal? ") )
procent = float( input("Wat is de intrest in procenten? "))
looptijd = int( input("Wat is de looptijd? "))

def RechtsUitlijnen( tekst, breedte ):
    # van de gewenste breedte de lengte van de tekst aftrekken
    breedte = breedte - len(str(tekst))
    # eerst een aantal spaties, en dan de tekst zelf
    return(" "*breedte + str(tekst))

# de kolomhoofdingen
print(RechtsUitlijnen("Jaar",8), RechtsUitlijnen("Kapitaal", 12), RechtsUitlijnen("Rente",8))

# de cijfers
for jaar in range(int(looptijd)):
    rente = round((kapitaal * procent / 100), 2)
    rente_format = format( rente, ".2f" )
    kapitaal_format = format( kapitaal, ".2f" )
    print( RechtsUitlijnen(jaar + 1, 8), RechtsUitlijnen(kapitaal_format, 12), RechtsUitlijnen(rente_format, 8) )
    kapitaal += rente


