def printWith2Decimals( getal ):
    global x
    print("dit getal is afgerond %.2f" % getal )
    x = 4                           # local scope / global scope
    print("x is in de functie", x)


x = 43/7
# print(format( x, ".2f" ) )
printWith2Decimals( x )
print("x is buiten de functie", x)