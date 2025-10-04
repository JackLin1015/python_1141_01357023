n = int(input("請輸入n:"))
print("請輸入數列:",end="")
num = list(map(int,input().split()))
num2 = []
num2.extend(num)
num2 = ' '.join(str(i)for i in num2)
print(f"排序前的數列:{num2}")
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(num[j]>num[j+1]):
            temp = num[j]
            num[j] = num[j+1]
            num[j+1] = temp
num = ' '.join(str(i)for i in num)
print(f"排序後的數列:{num}")