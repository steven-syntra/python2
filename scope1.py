# globale variabele a
a = 14

def MijnFunctie():
    global a
    # lokale variabele a
    a = 3
    print("Binnen de functie: ", a)

antwoord = MijnFunctie()

print(antwoord)
