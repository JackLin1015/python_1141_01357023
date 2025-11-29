def spiral_matrix(n):
    w = len(str(n * n))
    matrix = [[0] * n for _ in range(n)]
    if n % 2 == 1:
        x, y = n // 2, n // 2
    else:
        x, y = n // 2, n // 2 - 1
    num = 1
    matrix[x][y] = num
    num += 1
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    step_len = 1
    dir_idx = 0
    while num <= n * n:
        for _ in range(2):  
            dx, dy = directions[dir_idx]
            for _ in range(step_len):
                if num > n * n:
                    break
                x += dx
                y += dy
                matrix[x][y] = num
                num += 1
            dir_idx = (dir_idx + 1) % 4
        step_len += 1
    for row in matrix:
        print(" ".join(f"{n:>{w}}" for n in row))
n = int(input().strip())
spiral_matrix(n)
