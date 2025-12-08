import math
from sqlite3 import connect


def dist(a,b):
    x1,y1,z1 = a
    x2,y2,z2 = b
    return math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
def first(a):
    return a[0]

coords = []
with open("input.txt") as f:
    for line in f:
        l = line.strip().split(",")
        a,b,c = l
        coords.append((int(a),int(b),int(c)))

dists = []
for a in range(len(coords)):
    for b in range(a+1,len(coords)):
        dists.append((dist(coords[a],coords[b]),a,b))
sortedDists = sorted(dists, key=first)

circuits = []

for d in sortedDists:
    dist, a, b = d
    newCircuit = True

    aIndex = -1
    bIndex = -1
    for i in range(len(circuits)):
        foundA = a in circuits[i]
        foundB = b in circuits[i]
        if foundA and foundB:
            newCircuit = False
            break
        if foundA:
            aIndex = i
        if foundB:
            bIndex = i
    if aIndex != -1 and bIndex !=-1:
        aSet = circuits[aIndex]
        bSet = circuits[bIndex]
        combinedSet = aSet.copy()
        combinedSet.update(bSet)
        circuits = [c for i, c in enumerate(circuits) if i not in {aIndex,bIndex}]
        circuits.append(combinedSet)
    elif aIndex != -1:
        circuits[aIndex].add(b)
    elif bIndex != -1:
        circuits[bIndex].add(a)
    elif newCircuit:
        circuits.append({a, b})

    if len(circuits)==1 and len(circuits[0])==1000:
        print(coords[a], coords[b])
        print(coords[a][0]*coords[b][0])
        break
