with open("input.txt") as f:
    pos = 50
    count = 0
    for line in f:
        num = int(line[1:].strip())
        sign = (line[0]=="R") * 2 - 1

        pos += (sign*num)
        if (pos%100) == 0:
            count += 1

    print(count)