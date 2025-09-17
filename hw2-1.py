n = int(input("請輸入三角形高度:"))
if n > 0:
    for i in range(n):
        if(i == 0):
            for j in range(n):
                if(j != n-1):
                    print(" ",end="")
                else:
                    print("*",end="")
        elif i > 0 and i < n - 1:
            for j in range(n+i):
                if j == n - i - 1 or j == n + i - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
        else:
            for j in range(2*n-1):
                print("*",end="")
        print()
else:
    print("輸入錯誤")