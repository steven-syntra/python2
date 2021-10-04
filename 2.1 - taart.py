#dit programma berekent in hoeveel stukken een aantal taarten gesneden moeten worden
#om alle deelnemers een stuk te geven
bericht = "Je moet de taarten in %s stukken snijden."

aantal_taarten = 15
aantal_deelnemers = 90

aantal_stukken = aantal_deelnemers // aantal_taarten

print(bericht % int(aantal_stukken))