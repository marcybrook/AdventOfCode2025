
def getMaxNumber(s, count):
    if count == 0:
        return ""
    for i in "987654321":
        loc = s[0:len(s)+1-count].find(i)
        if loc != -1:
            return s[loc] + getMaxNumber(s[loc+1:], count-1)


with open("input.txt") as f:
    total = 0
    for line in f:
        m = getMaxNumber(line.strip(), 12)
        print(line.strip(), m)
        total+=int(m)
    print(total)