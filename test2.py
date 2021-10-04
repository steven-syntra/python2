import math

straal = int( input("Wat is de straal? "))
oppervlakte = straal**2 * math.pi

print("De oppervlakte van de cirkel met straal %d is %f" % ( straal, oppervlakte))