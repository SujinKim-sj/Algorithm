# 바텀업 방식
n = int(input())
dp = [0 for i in range(1000010)]

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 0

for i in range(5, n + 1):
    if dp[i - 1] == 0 or dp[i - 2] == 0 or dp[i - 3] == 0:
        dp[i] = 1
    else:
        dp[i] = 0

if dp[n] == 1:
    print("YES")
else:
    print("NO")
    
    
# 탑다운 방식
import sys

sys.setrecursionlimit(10 ** 6)


def recur(x):
    ret = 0
    if x < 0:
        return -1
    if x == 0:
        return 0

    if dp[x] != -1:
        return dp[x]

    for i in range(1, 4):
        if recur(x - i) == 0:
            ret = 1

    dp[x] = ret
    return dp[x]


n = int(input())
dp = [-1 for i in range(1000010)]

if recur(n) == 1:
    print("YES")
else:
    print("NO")