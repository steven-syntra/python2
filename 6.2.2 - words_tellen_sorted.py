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

# OUTPUT
print("Van veel naar weinig:")
#door de dictionary lopen, gesorteerd op waarde van hoog naar laag
# zie https://able.bio/rhett/sort-a-python-dictionary-by-value-or-key--84te6gv
for letter, aantal in sorted(d.items(), key=lambda kv: kv[1], reverse=True):
    print("%s woorden beginnen met de letter %s " % (aantal, letter ))