# INITIALISATIE
fp = open('words.txt')
d = {}                           # een lege dictionary: de letters zijn de sleutels, de aantallen zijn de waarden
                                     # dus: { "a" : 6778, "b" : 8955, ...

# PROCESSING
#alle woorden overlopen
for line in fp:

    beginletter = line[0]   #eerste letter van het woord nemen

    if beginletter in d:
        d[beginletter] += 1
    else:
        d[beginletter] = 1

    # if beginletter == vorigeletter: #zelfde beginletter als het vorige woord?
    #     tel += 1                                 #teller verhogen
    # else:                                          #nieuwe beginletter?
    #     d[vorigeletter] = tel   #teller wegschrijven in dictionary met als sleutel de (vorige) letter
    #     tel=1                           #teller weer op 1 zetten
    #
    # vorigeletter = beginletter #vorige beginletter onthouden
    #einde lus

#d[vorigeletter] = tel   #laatste letter (z) wegschrijven

# OUTPUT
print("Alfabetisch:")
#door de dictionary lopen en lijn per lijn printen
for letter, aantal in d.items():
  print("%s woorden beginnen met de letter %s " % (aantal, letter))