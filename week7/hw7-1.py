def Sum(d1, d2, use):
    s = 0
    for i in range(d1 - 1, d2):
        s += use[i]
    return s

def Max(d1, d2, use):
    ma = use[d1 - 1]
    for i in range(d1, d2):
        if use[i] > ma:
            ma = use[i]
    return ma

def Min(d1, d2, use):
    mi = use[d1 - 1]
    for i in range(d1, d2):
        if use[i] < mi:
            mi = use[i]
    return mi

num = int(input())
data = list(map(int, input().split()))
time = int(input())

for _ in range(time):
    inst = input().split()
    r1 = int(inst[1])
    r2 = int(inst[2])
    if inst[0] == "SUM":
        print(Sum(r1, r2, data))
    elif inst[0] == "MAX":
        print(Max(r1, r2, data))
    else:
        print(Min(r1, r2, data))
