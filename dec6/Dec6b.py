def product(arr):
    t = 1
    for v in arr:
        t*=v
    return t

with open("input.txt") as f:
    rows = []
    for line in f:
        rows.append(line.strip("\n"))

    a,b,c,d,op = rows
    total = 0
    mem = []
    for i in range(len(rows[0])-1,-1,-1):
        v = a[i] + b[i] + c[i] + d[i]
        if len(v.strip()) != 0:
            mem.append(int(v))
        if op[i] == "+":
            total += sum(mem)
            mem = []
        if op[i] == "*":
            total += product(mem)
            mem = []


    print(total)