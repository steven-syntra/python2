import random


def DeelbaarDoor(getal, deler):
    # deze functie controleert of het getal deelbaar is door de deler
    if getal % deler == 0:
        return True
    else:
        return False


for i in range(20):
    x = random.randint(100, 999)
    if DeelbaarDoor(x, 7):
        print("%s is deelbaar door 7" % x)
    else:
        print(x)
