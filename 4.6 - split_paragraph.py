tekst = \
    "Ruim 50.000 kandidaten hengelen in Vlaanderen naar uw stem en hopen straks " \
    "gemeenteraadslid te worden. Het is maar de vraag of ze zo blij gaan zijn als die " \
    "droom in vervulling gaat. De inzet van de lokale verkiezingen, op 14 oktober, is " \
    "heel precies in cijfers vastgelegd: er moeten 7.398 nieuwe gemeenteraadsleden " \
    "verkozen worden, verspreid over de 308 Vlaamse gemeenten, plus 175 nieuwe " \
    "provincieraadsleden."

#initialisatie tellers
begin_of_line=0                         #start van de eerste regel = 0
end_of_line=0                           #einde van de eerste regel is - voorlopig! - 0

# de tekst letter per letter overlopen
for cursor in range(len(tekst)):

    # als de cursor meer dan 40 karakters ver is (van het begin van de lijn)
    if ( cursor - begin_of_line ) > 40:
        # dan is de output het stuk tekst van begin_of_line tot end_of_line
        print( tekst[begin_of_line:end_of_line] )
        # begin_of_line wordt nu: 1 positie verder dan het einde vd vorige lijn
        begin_of_line = end_of_line + 1                  

    # als we een spatie tegenkomen, is dat (voorlopig) het nieuwe einde van de lijn;
    # dat einde schuift dus op telkens wanneer we een spatie tegenkomen
    if tekst[cursor] == " ":
        end_of_line = cursor


# als we uit de lus komen, nog het laatste stuk tekst printen tot op het einde
# (en niet tot aan de laatste spatie !)
print( tekst[begin_of_line:] )



