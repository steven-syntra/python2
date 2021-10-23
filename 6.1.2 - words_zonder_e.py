fp = open("words.txt", "r")


def HeeftEenE(woord):
    if "e" in woord:
        return True
    else:
        return False


for line in fp:
    line = line.strip()
    if not HeeftEenE(line):
        print(line)
