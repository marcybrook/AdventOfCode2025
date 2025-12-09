# Get tiles (in given space)
tiles = []
with open("input.txt") as f:
    for line in f:
        a,b = line.strip().split(",")
        tiles.append((int(a),int(b)))

# Get all rectangles (in given space)
rectangles = []
for a in range(len(tiles)):
    for b in range(a+1,len(tiles)):
        rectangles.append((tiles[a],tiles[b]))

# Create given space to minspace map
xVals = set()
yVals = set()
for t in tiles:
    x, y = t
    xVals.add(x)
    yVals.add(y)
xVals = sorted(xVals)
yVals = sorted(yVals)
xMap = dict()
for i in range(len(xVals)):
    xMap[xVals[i]] = i
yMap = dict()
for i in range(len(yVals)):
    yMap[yVals[i]] = i

# Creating editable map
printout = [["." for x in range(xMap[xVals[-1]]+1) ] for y in range(yMap[yVals[-1]]+1) ]

# Populating map with vertical lines
for i in range(len(tiles)):
    tileA, tileB = tiles[i], tiles[(i + 1) % len(tiles)]
    for y in range(min(yMap[tileA[1]],yMap[tileB[1]]), max(yMap[tileA[1]],yMap[tileB[1]])+1):
        for x in range(min(xMap[tileA[0]], xMap[tileB[0]]), max(xMap[tileA[0]], xMap[tileB[0]]) + 1):
            printout[y][x] = "#"

# Fill in the map
def fill(po, x, y):
    queue = [(x,y)]
    while len(queue)>0:
        x,y = queue.pop()
        if po[y][x] == ".":
            po[y][x] = "#"
            queue.append((x+1, y))
            queue.append((x, y+1))
            queue.append((x-1, y))
            queue.append((x, y-1))
fill(printout,100,100)

# Filter rectangles
allowedRectangles = []
count = 0
for r in rectangles:
    count+=1
    if count %1000==0:
        print(count,"/",len(rectangles))
    corner1, corner2 = r
    minX = min(corner1[0],corner2[0])
    minY = min(corner1[1],corner2[1])
    maxX = max(corner1[0],corner2[0])
    maxY = max(corner1[1],corner2[1])
    area = (maxX-minX+1)*(maxY-minY+1)
    keep = True
    for y in range(yMap[minY], yMap[maxY]+1):
        for x in range(xMap[minX], xMap[maxX]+1):
            if printout[y][x]==".":
                keep = False
                break
        if not keep:
            break
    if keep:
        allowedRectangles.append(area)

# Output
print(sorted(allowedRectangles,reverse=True))
