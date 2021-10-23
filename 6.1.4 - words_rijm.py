import functie_rijm as rijm

fp = open('words.txt')
suffix = input("Waarop moeten de woorden rijmen? ")

# alle woorden overlopen
for line in fp:
    word = line.strip()
    # enkel woorden die op de opgegeven suffix eindigen weergeven
    if rijm.RijmtOp(word, suffix):
        print(word)
