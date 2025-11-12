class ma:
    def scan(matrix):
        global n
        n = int(input())
        matrix.clear()
        for i in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)

    def print(matrix):
        if not matrix:  
            print("No element in matrix can be printed.")
            return
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                print(matrix[i][j], end=" ")
            print()

    def rotater(matrix):
        if not matrix:  
            print("No element in matrix can be rotated.")
            return
        for i in range(n): 
            for j in range(i+1, n): 
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
        m = len(matrix[0]) 
        for i in range(n): 
            for j in range(m//2): 
                matrix[i][j], matrix[i][m-j-1] = matrix[i][m-j-1], matrix[i][j]

    def rotatel(matrix):
        if not matrix: 
            print("No element in matrix can be rotated.")
            return
        for i in range(n): 
            for j in range(i+1, n): 
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
        for i in range(n//2): 
            matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]
            
list1 = []
while True:
    mode = input().strip()
    if mode == "stop":
        break
    elif mode == "scan":
        ma.scan(list1)
    elif mode == "rotate right":
        ma.rotater(list1)
    elif mode == "rotate left":
        ma.rotatel(list1)
    elif mode == "print":
        ma.print(list1)
