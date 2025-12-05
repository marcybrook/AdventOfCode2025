def first(n):
    return n[0]

def mergeRanges(ranges):
    ranges = sorted(ranges, key=first)
    newRanges = []
    cMin, cMax = ranges[0]
    for r in ranges:
        nMin, nMax = r
        if nMin <= cMax+1 :
            cMax = max(nMax,cMax)
        else:
            newRanges.append((cMin,cMax))
            cMax = nMax
            cMin = nMin
    newRanges.append((cMin, cMax))

    return newRanges

with open("input.txt") as f:
    ranges = []
    for line in f:
        sp = line.strip().split("-")
        if len(sp) == 2:
            ranges.append((int(sp[0]),int(sp[1])))

    x = len(ranges)
    newRanges = mergeRanges(ranges)

    for s in sorted(ranges, key=first):
        print(s, end= " ")
        for t in newRanges:
            if s[0] == t[0]:
                print(t, end="")
        print()
    input()

    diffs = [x[1]-x[0]+1 for x in newRanges]
    oldMax = 0
    for i in range(len(newRanges)):
        print(oldMax<newRanges[i][0])
        print(newRanges[i],diffs[i])
    print(sum(diffs))