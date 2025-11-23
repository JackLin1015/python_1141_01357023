def count_paths(grid, n):
    visited = [[False]*n for _ in range(n)]
    directions = [(1,0), (-1,0), (0,1), (0,-1)] 
    def dfs(x, y):
        if x == n-1 and y == n-1:
            return 1
        visited[x][y] = True
        total_paths = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == 0 and not visited[nx][ny]:
                    total_paths += dfs(nx, ny)
        visited[x][y] = False  
        return total_paths
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return 0
    return dfs(0, 0)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
print(count_paths(grid, n))
