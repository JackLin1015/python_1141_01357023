list1 = []
count  = 0
while True:
    num = int(input())
    if num == 0:
        break    
    list1.append(num)
    count += 1
for i in range(count):
    sum = 0
    faken = list1[i]
    while(faken % 3 != 0):
        faken += 1
    while(faken != 0):
        sum += faken // 3
        faken //= 3
    print(sum + list1[i])
