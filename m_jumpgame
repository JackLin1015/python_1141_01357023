def canJump(nums):
    n = len(nums)
    reachable = [False] * n
    reachable[0] = True 
    for i in range(n):
        if not reachable[i]:
            continue
        step = nums[i]
        for j in range(1, step + 1):
            if i + j < n:
                reachable[i + j] = True
    return reachable[-1]

nums = list(map(int,input().split(",")))
print(str(canJump(nums)).lower())
