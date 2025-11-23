T = input()
C = input()
n = len(T)
m = len(C)
if m == 0:
    total = n * 0.3
    x = int(total * 10 + 0.5) / 10
    print("%.1f" % x)
else:
    INF = 10**18
    dp = [INF] * (n + 1)
    dp[0] = 0.0
    for i in range(n):
        cost_type = dp[i] + 0.3
        if cost_type < dp[i+1]:
            dp[i+1] = cost_type
        if i + m <= n:
            match = True
            for k in range(m):
                if T[i+k] != C[k]:
                    match = False
                    break
            if match:
                cost_paste = dp[i] + 0.4
                if cost_paste < dp[i+m]:
                    dp[i+m] = cost_paste
    ans = dp[n]
    ans = int(ans * 10 + 0.5) / 10
    print("%.1f" % ans)
