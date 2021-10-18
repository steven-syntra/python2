student =	{
"voornaam": "Jan",
"naam": "Janssens",
"straat": "Oude baan",
"huisnr": "22",
"postcode": 2800,
"gemeente": "Mechelen",
"geboortedatum": "14/05/1991",
"telefoon": "015 24 24 26",
"e-mail": "jan.janssens@gmail.com"
}

def StudentToTable( student ):
    """ Deze functie vormt een dictionary 'student' om naar een HTML tabel """

    print("<h1>Student</h1>") # hoofding
    print("<table>") # start van de tabel

    # voor elk gegeven (naam, voornaam, ...) een rij (<tr>) toevoegen met 2 cellen (<td>)
    for key, value in student.items():
        # de velden krijgen als eerste letter een hoofdletter (Naam, Voornaam, enz...)
        #print("<tr><td>" + str(key[0].upper()) + str(key[1:]) + "</td><td>" + str(value) + "</td></tr>")
        print("<tr><td>" + key.capitalize() + "</td><td>" + str(value) + "</td></tr>")

    print("</table>") # afsluiten van de tabel

# de funtie oproepen voor de student dictionary
StudentToTable( student )