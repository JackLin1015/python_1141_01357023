def max_cola(list1, count):
    for i in range(count):
        n = list1[i]
        total = n
        empty = n
        while empty >= 3:
            new = empty // 3
            total += new
            empty = empty % 3 + new
        if empty == 2:
            total += 1  
        print(total)
list1 = []
count = 0
while True:
    num = int(input())
    if num == 0:
        break
    list1.append(num)
    count += 1
max_cola(list1, count)