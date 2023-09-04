# 바텀업 방식
n = int(input())
dp = [0 for i in range(1000010)]

dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 1

for i in range(5, n + 1):
    if dp[i - 1] == 0 or dp[i - 3] == 0 or dp[i - 4] == 0:
        dp[i] = 1
    else:
        dp[i] = 0

if dp[n] == 1:
    print("YES")
else:
    print("NO")
