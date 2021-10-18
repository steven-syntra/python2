stemmen =	{
"NVA": 2455,
"SP-A": 2856,
"CD&V": 1501,
"GROEN": 1744,
"OPEN-VLD": 1988,
"VLAAMSBELANG": 586,
"PVDA": 697
}

def LU( tekst, breedte ):
    """ tekst links uitlijnen door er achteraan spaties aan toe te voegen"""
    breedte -= int(len(str(tekst)))
    return(str(tekst) + " "*breedte)

def RU( tekst, breedte ):
    """ tekst rechts uitlijnen door er vooraan spaties aan toe te voegen"""
    breedte -= int(len(str(tekst)))
    return(" "*breedte + str(tekst))

#totaal van de stemmen maken
totaal=0
for partij, aantal in stemmen.items():
    totaal += aantal

print("Totaal aantal stemmen: %s" % totaal)
print("")

#per partij het percentage berekenen en naam + percentage printen
totprocent = 0 # controlevariabele totaal van de percentages
for partij, aantal in stemmen.items():
    # berekeningen
    float_procent = aantal * 100 / totaal
    totprocent += float_procent
    # bewerkingen (teksten formatteren)
    string_procent = '{0:.2f}'.format(float_procent) # percentage altijd met 2 decimalen
    partij_left_aligned = LU(partij,25) # partij links uitlijnen
    procent_right_aligned = RU(string_procent, 25) # percentage rechts uitlijnen
    #output
    print("%s %s" % (partij_left_aligned, procent_right_aligned))

print("")
print("%s %s" % (LU("Totaal van de percentages:", 40) , RU('{0:.2f}'.format(totprocent),10)))