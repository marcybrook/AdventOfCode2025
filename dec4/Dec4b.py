def process(rollMap):
    newMap=[]
    for y in range(len(rollMap)):
        newRow = []
        for x in range(len(rollMap[y])):
            newRow.append(countRolls(rollMap,x,y))
        newMap.append(newRow)
    return newMap

def countRolls(rollMap, x, y):
    offset = [-1,0,1]
    exclude = [(0,0)]
    count = 0
    for dx in offset:
        for dy in offset:
            if (dx, dy) not in exclude:
                newY = y+dy
                newX = x+dx
                if newY in range(len(rollMap)) and newX in range(len(rollMap[newY])) and rollMap[newY][newX] == '@':
                    count += 1
    return count

def decrementRolls(countMap, x, y):
    offset = [-1,0,1]
    exclude = [(0,0)]
    for dx in offset:
        for dy in offset:
            if (dx, dy) not in exclude:
                newY = y+dy
                newX = x+dx
                if newY in range(len(countMap)) and newX in range(len(countMap[newY])):
                    countMap[newY][newX] = countMap[newY][newX] -1


with open("input.txt") as f:
    rollMap = []
    for line in f:
        rollMap.append(list(line.strip()))

    countMap = process(rollMap)
    oldCount=-1
    newCount=0
    while newCount != oldCount:
        oldCount = newCount
        for y in range(len(rollMap)):
            for x in range(len(rollMap[y])):
                if rollMap[y][x] == "@" and countMap[y][x]<4:
                    rollMap[y][x] = "."
                    decrementRolls(countMap,x,y)
                    newCount+=1



    for y in range(len(rollMap)):
        for x in range(len(rollMap[y])):
            if rollMap[y][x] == '.':
                print(".", end="")
            else:
                if countMap[y][x]<4:
                    print("x", end="")
                else:
                    print("@",end="")
        print()
    print(newCount)