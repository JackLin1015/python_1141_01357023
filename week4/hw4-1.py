def gcd(i,j):
    list1 = []
    if(i > j):
        for k in range(1,j+1):
            if i % k == 0 and j % k == 0:
                list1.append(k)
        return max(list1)
    elif(i == j):
        return i           
    else:
        for k in range(1,i+1):
            if j % k == 0 and i % k == 0:
                list1.append(k)
        return max(list1)

for times in range(100):
    data = int(input())
    if data == 0:
        break
    g = 0
    for i in range(1,data):
        for j in range(i+1,data+1):
            g += gcd(i,j)
    print(g)