from sys import stdin
n = int(stdin.readline())
dp = []
for _ in range(n):
    dp.append(list(map(int, stdin.readline().split())))
dp.append([0]*(n+1))


def choice_one(i):
    global n
    dp[i+1][0] = dp[i][0] + dp[i + 1][0]
    last = len(dp[i]) - 1
    dp[i+1][-1] = dp[i][last] + dp[i + 1][last + 1]

    for j in range(i):
        dp[i+1][j+1] = dp[i+1][j+1] + max(dp[i][j], dp[i][j + 1])

    if i < n-1:
        choice_one(i+1)


choice_one(0)
print(max(dp[-2]))