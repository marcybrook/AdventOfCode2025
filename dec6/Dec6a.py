with open("input.txt") as f:
    rows = []
    for line in f:
        rows.append(line.strip().split())

    total = 0
    for i in range(len(rows[0])):
        a,b,c,d,op = rows
        if op[i] == "*":
            total += int(a[i])*int(b[i])*int(c[i])*int(d[i])
        if op[i] == "+":
            total += int(a[i])+int(b[i])+int(c[i])+int(d[i])

    print(total)