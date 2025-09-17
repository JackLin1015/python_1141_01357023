n = int(input("請輸入矩陣高度:"))
count = 1
count2 = 0
c = 1
for i in range(1,n+1):
    for j in range(i):
        c += 1
while True:
    c = c // 10
    count2 += 1
    if c == 0:
        break
if n > 0:
    for i in range(1,n+1):
        for j in range(i):
            print(f"{count:>{count2}}",end=" ")
            count += 1
        if(i != n):
            print()
else:
    print("輸入錯誤")               