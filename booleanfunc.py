def HetIsGroen( dier ):
    if dier == "kikker" or dier == "krokodil":
        return True
    else:
        return False

antwoord = HetIsGroen("paard")
print(antwoord)
antwoord = HetIsGroen("kikker")
print(antwoord)
antwoord = HetIsGroen("koe")
print(antwoord)
antwoord = HetIsGroen("everzwijn")
print(antwoord)
antwoord = HetIsGroen("krokodil")
print(antwoord)
