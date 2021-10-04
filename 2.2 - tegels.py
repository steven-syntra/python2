import math

#dit programma berekent hoeveel tegels er nodig zijn om de vloer van een kamer te betegelen
#voor een kamer en tegels met opgegeven afmetingen
lengte_kamer = 7
breedte_kamer = 5
tegel_x = 0.3
tegel_y = 0.3

tegels_in_de_lengte = math.ceil(lengte_kamer / tegel_x)
tegels_in_de_breedte = math.ceil(breedte_kamer / tegel_y)

aantal_tegels = tegels_in_de_lengte * tegels_in_de_breedte

bericht = "Je moet %d tegels van %.2f x %.2f meter kopen voor een kamer van %.2f op %.2f meter."
print(bericht % (int(aantal_tegels), tegel_x, tegel_y, lengte_kamer, breedte_kamer))
