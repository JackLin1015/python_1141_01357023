n = int(input())
while True:
    if n == 0:
        break
    while True:
        train = list(map(int, input().split()))
        if train == [0]:
            break
        stack = []
        index = 0 
        for i in range(1, n + 1):  
            stack.append(i)
            while stack and stack[-1] == train[index]:
                stack.pop()
                index += 1
        print("YES" if not stack else "NO")