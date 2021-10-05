def RechtsUitlijnen(tekst, breedte):
    """ docstring
    Deze functie lijnt een opgegeven tekst rechts uit op de opgegeven
    breedte ; de ruimte links van de tekst wordt opgevuld met spaties
    """
    # van de gewenste breedte de lengte van de tekst aftrekken
    aantal_spaties = breedte - len(tekst)
    # eerst een aantal spaties, en dan de tekst zelf printen
    print(" " * aantal_spaties + tekst)


RechtsUitlijnen("banaan", 70)
RechtsUitlijnen("nog een banaan", 70)
RechtsUitlijnen("2.30 €", 70)
RechtsUitlijnen("dit is een hele lange zin", 70)
RechtsUitlijnen("14.10 €", 70)
