# een lijst met 3 student-dictionaries erin
studenten = [
                    { "voornaam": "Jan",  "naam": "Janssens",  "straat": "Oude baan",  "huisnr": "22",  "postcode": 2800,  "gemeente": "Mechelen",
                    "geboortedatum": "14/05/1991", "telefoon": "015 24 24 26", "e-mail": "jan.janssens@gmail.com" },
                    { "voornaam": "Piet", "naam": "Peeters", "straat": "Molenlei", "huisnr": "3", "postcode": 2100, "gemeente": "Deurne",
                     "geboortedatum": "7/7/1992", "telefoon": "03 14 15 78", "e-mail": "piet.peeters@microsoft.com"},
                    { "voornaam": "Mieke", "naam": "Verlinden", "straat": "Lentelei", "huisnr": "18B", "postcode": 2640, "gemeente": "Mortsel",
                     "geboortedatum": "28/7/1993", "telefoon": "03 99 65 44", "e-mail": "mieke_verlinden@bol.com"}
                    ]

def StudentToTable( studenten ):
    # alle studenten (dictionaries) overlopen
    for student in studenten:
        print("<h1>Student</h1>")  # hoofding
        print("<table>")  # start van de tabel

        # voor elk gegeven (naam, voornaam, ...) een rij (<tr>) toevoegen met 2 cellen (<td>)
        for key, value in student.items():
            # de velden krijgen als eerste letter een hoofdletter (Naam, Voornaam, enz...)
            print("<tr><td>" + key.capitalize() + "</td><td>" + str(value) + "</td></tr>")

        print("</table>")  # afsluiten van de tabel

StudentToTable( studenten )