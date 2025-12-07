def combineRays(incoming, existing):
    if existing == ".":
        return incoming
    for key in incoming:
        if key in existing:
            existing[key] = existing[key] + incoming[key]
        else:
            existing[key] = incoming[key]
    return existing

def splitRay(incoming):
    outgoing = {}
    for key in incoming:
        outgoing[key+1] = incoming[key]
    return outgoing

rows = []
with open("input.txt") as f:
    for line in f:
        row = []
        for c in line.strip():
            row.append(c)
        rows.append(row)

count = 0
for level in range(1,len(rows)):
    for x in range(len(rows[level])):
        above = rows[level-1][x]
        if above == "S":
            rows[level][x] = {0:1}
        elif above != "." and above != "^":
            here = rows[level][x]
            if here == "^":
                left = rows[level][x - 1]
                right = rows[level][x + 1]
                splitAbove = splitRay(above)
                count+=1
                rows[level][x - 1] = combineRays(splitAbove.copy(), left)
                rows[level][x + 1] = splitAbove.copy()
            else:
                rows[level][x] = combineRays(above.copy(),here)

for row in rows:
    for x in row:
        print("{:<12}".format(str(x)), end="")
    print()

# Solution 1
print(count)

# Solution 2
total = 0
for c in rows[-1]:
    if c != ".":
        for key in c:
            val = c[key]
            total += val
print(total)