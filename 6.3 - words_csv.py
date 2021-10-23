inputfile = open('words.txt')
outputfile = open('words.csv', "w")

tel = 1
vorige_eerste_letter = ""
output = ""

inhoud_bestand = ""

#alle woorden overlopen
for line in inputfile:
    
    woord = line.strip()                  #newline weghalen
    eerste_letter = woord[0]       #de eerste letter van het woord nemen
    
    if tel == 6:                                                            #bij het 6de woord
        print(output)                                                           #output tonen
        inhoud_bestand += output + "\n"
        output = ""                                                               #output leegmaken
        
    #bij een nieuwe beginletter (behalve bij de "a")
    if eerste_letter != vorige_eerste_letter and vorige_eerste_letter > "":
        tel = 1     #opnieuw woorden beginnen tellen 
    
    #bij de eerste 5 woorden, het woord toevoegen aan de output gevolgd door een  ";"
    if tel <= 5:
        output += woord + ";"
        
    #bij elk woord
    tel += 1                                                                    #woordenteller verhogen
    vorige_eerste_letter = eerste_letter              #eerste letter onthouden

outputfile.write(inhoud_bestand)                                #output wegschrijven naar bestand