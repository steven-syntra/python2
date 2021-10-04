a="10"
b=6
c=int(a)*b              #type conversion string -> int
dagen14 = 589646

# + is de concatenation operator
print("14 dagen is hetzelfde als %s minuten en %s seconden" % ("806" , str(dagen14)) ) #type conversion int -> string
print(c)
print(type(c))

if c > 20:
    print("C is nu wel erg groot hoor!")
else:
    print("C blijft behoorlijk klein")


#functie definitie
def Print8Times( tekst ):       # een functie met een parameter
    print(tekst)
    print(tekst)
    print(tekst)
    print(tekst)
    print(tekst)
    print(tekst)
    print(tekst)
    print(tekst)
    # einde van de functie definitie


print("================")

Print8Times( "Iets totaal anders" ) # function call met een argument