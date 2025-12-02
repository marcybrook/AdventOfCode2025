allRanges = []

with open("input.txt") as f:
    for line in f:
        ranges = line.strip().split(",")
        for r in ranges:
            a,b = r.split("-")
            allRanges.append((a,b))

i = 0
while i < len(allRanges):
    r = allRanges[i]
    a, b = r
    if len(a) == len(b):
        if len(a)%2==1:
            allRanges.remove(r)
        else:
            i += 1
    else:
        allRanges.remove(r)
        allRanges.append((a, "9"*len(a)))
        allRanges.append(("1"+("0"*len(a)), b))

answers = set()
for r in allRanges:
    a,b = r
    start = int(a[0:int(len(a)/2)])
    end = int(b[0:int(len(b)/2)])
    for i in range(start,end+1):
        candidate = str(i) + str(i)
        if int(b) >= int(candidate) >= int(a):
            answers.add(candidate)

runningTotal = 0
for a in answers:
    runningTotal += int(a)

print(runningTotal)