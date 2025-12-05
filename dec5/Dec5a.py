with open("input.txt") as f:
    ranges = []
    vals = []
    for line in f:
        sp = line.strip().split("-")
        if len(sp) == 2:
            ranges.append((int(sp[0]),int(sp[1])))
        if len(sp) == 1 and sp[0] != "":
            vals.append(int(sp[0]))

    count = 0
    for v in vals:
        for r in ranges:
            if r[0]<v<r[1]:
                print(v,r)
                count+=1
                break

    print(count)