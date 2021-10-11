kapitaal = int( input("Wat is het kapitaal? ") )
procent = float( input("Wat is de intrest in procenten? "))
looptijd = int( input("Wat is de looptijd? "))
eriseenlimiet = False
limiet = 0

if  input("Is er een limiet? ") == "y":
    eriseenlimiet = True
    limiet = int( input("Wat is de limiet? "))

def LimietBereikt(kapitaal):
    global limiet
    if eriseenlimiet and kapitaal >= limiet:
        return True

def R_Align( tekst, breedte ): # rechts uitlijnen
    breedte = breedte - len(str(tekst))
    return(" "*breedte + str(tekst)) # eerst een aantal spaties en dan de tekst

# de kolomhoofdingen
print(R_Align ("Jaar",8), R_Align ("Kapitaal", 12), R_Align ("Rente",8))

# de cijfers
for jaar in range(int(looptijd)):
    if LimietBereikt(kapitaal):
        break
    rente = round((kapitaal * procent / 100), 2)
    rente_f = format( rente, ".2f" )
    kapitaal_f = format( kapitaal, ".2f" )
    print( R_Align (jaar + 1, 8), R_Align (kapitaal_f, 12), R_Align (rente_f, 8) )
    kapitaal += rente



