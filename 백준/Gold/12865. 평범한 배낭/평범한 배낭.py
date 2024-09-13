from sys import stdin

N, K = tuple(map(int, stdin.readline().split()))
things = [tuple(map(int, stdin.readline().split())) for _ in range(N)]

dp = [[0] * (K+1) for _ in range(N+1)]


for i in range(1, N + 1):
    for k in range(1, K + 1):
        if things[i - 1][0] <= k:
            dp[i][k] = max(things[i - 1][1] + dp[i - 1][k - things[i - 1][0]], dp[i - 1][k])
        else:
            dp[i][k] = dp[i - 1][k]

print(dp[N][K])