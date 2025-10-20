def gcd(i,j):
    if j == 0:
        return i
    else:
        return gcd(j,i%j)

for times in range(100):
    data = int(input())
    if data == 0:
        break
    g = 0
    for i in range(1,data):
        for j in range(i+1,data+1):
            g += gcd(i,j)
    print(g)