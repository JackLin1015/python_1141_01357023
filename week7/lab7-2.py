n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
pattern = input()
use = [ch for ch in pattern.strip().upper() if ch.isalpha()]
for w in use:
    if w == 'R':
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        m = len(matrix[0])  
        for i in range(n):
            for j in range(m//2):
                matrix[i][j], matrix[i][m-j-1] = matrix[i][m-j-1], matrix[i][j]
    elif w == 'H':
        for i in range(n//2):
            matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]
    else:
        m = len(matrix[0])  
        for i in range(n):
            for j in range(m//2):
                matrix[i][j], matrix[i][m-j-1] = matrix[i][m-j-1], matrix[i][j]
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end = " ")
    print()


