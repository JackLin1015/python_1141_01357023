num = []
count = 0
while True:
    try:   
        n = int(input("請輸入一個數:"))
        count += 1
        if(n == EOFError):
            break
        num.append(n)
        for i in range(len(num)-1):
            for j in range(len(num)-i-1):
                if num[j] > num[j+1]:
                    temp = num[j]
                    num[j] = num[j+1]
                    num[j+1] = temp
        if(count % 2 == 1):
            print(num[count//2])
        else:
            print((num[count//2-1]+num[count//2])//2)
    except ValueError:
        break
    except EOFError:
        break