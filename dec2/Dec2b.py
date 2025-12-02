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
        i += 1
    else:
        allRanges.remove(r)
        allRanges.append((a, "9"*len(a)))
        allRanges.append(("1"+("0"*len(a)), b))

answers = set()
for r in allRanges:
    a,b = r
    print(r, len(a))
    for i in range(2,len(a)+1):
        if len(a)%i == 0:
            start = int(a[0:int(len(a)/i)])
            end = int(b[0:int(len(b)/i)])
            print(start,end,i)
            for j in range(start,end+1):
                candidate = str(j) * i
                print(candidate, int(b) >= int(candidate) >= int(a))
                if int(b) >= int(candidate) >= int(a):
                    answers.add(candidate)

runningTotal = 0
for a in answers:
    runningTotal += int(a)

print(runningTotal)