#dit programma berekent in hoeveel stukken een aantal taarten gesneden moeten worden
#om alle deelnemers een stuk te geven
aantal_taarten = 6
aantal_deelnemers = 153

bericht0 = "Je hebt %s taarten voor %s deelnemers."
bericht1 = "Je moet %s taarten in %s stukken snijden."
bericht2 = "En %s taarten in %s stukken."

# t2 = het aantal taarten met 1 stuk meer
t2 = aantal_deelnemers % aantal_taarten

# de andere taarten (t1) hebben 1 stuk minder
t1 = aantal_taarten - t2

# aantal_stukken_1 = het aantal 'grotere' stukken per taart
aantal_stukken_1 = aantal_deelnemers // aantal_taarten

# aantal_stukken_2 = het aantal 'kleinere' stukken per taart
aantal_stukken_2 = aantal_stukken_1 + 1

print(bericht0 % ( aantal_taarten , aantal_deelnemers))
print(bericht1 % ( t1 , int(aantal_stukken_1) ))

if ( t2 != 0 ):
    print(bericht2 % ( t2 , int(aantal_stukken_2) ))

