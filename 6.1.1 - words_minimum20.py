fp = open("words.txt", "r")

for line in fp:
    line = line.strip()
    if len(line) >= 20:
        print(line)

