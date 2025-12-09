def area(a,b):
    x1,y1=a
    x2,y2=b
    return abs((x1-x2+1)*(y1-y2+1))

tiles = []

with open("input.txt") as f:
    for line in f:
        a,b = line.strip().split(",")
        tiles.append((int(a),int(b)))

best = 0
for a in range(len(tiles)):
    for b in range(a+1,len(tiles)):
        x = area(tiles[a],tiles[b])
        if x>best:
            best= x

print(best)