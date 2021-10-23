fp = open("words.txt", "r")


def HeeftEenLetterUitLijst(woord, lijst):
    for letter in lijst:
        if letter in woord:
            return True
    return False


lijst1 = ["a", "e", "o"]
lijst2 = ["n", "s", "t", "v", "w"]

for line in fp:
    line = line.strip()
    # lijst1 of lijst2 gebruiken als argument
    if not HeeftEenLetterUitLijst(line, lijst1):
        print(line)

