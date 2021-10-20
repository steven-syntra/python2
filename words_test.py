f = open("words.txt", "r")
outputfile = open('resultaat.txt', "a")

inhoud_bestand = ""
teller=0

for line in f:
    if len(line.strip()) > 20:
        teller += 1
        inhoud_bestand += (line.strip()) + "\n"

eindmsg = "Er zijn %d woorden die langer zijn dan 20 tekens"
inhoud_bestand += (eindmsg % teller)
outputfile.write(inhoud_bestand)


