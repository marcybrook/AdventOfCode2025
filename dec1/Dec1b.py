with open("input.txt") as f:
    pos = 50
    count = 0
    for line in f:
        num = int(line[1:].strip())
        sign = (line[0]=="R") * 2 - 1

        remainder = num%100
        count += (num-remainder)/100
        num = remainder

        oldPos = pos
        newPos = (pos + (sign*num)) % 100
        if newPos == 0:
            count += 1
        elif oldPos != 0 and newPos != (pos + (sign*num)):
            count += 1
        pos = newPos

    print(count)