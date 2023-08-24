import sys
sys.setrecursionlimit(10 ** 6)

def recur(sum):
    ret = 0
    if sum > n:
        return 0
    if sum == n:
        return 1
    if dp[sum] != -1:
        return dp[sum]

    for i in range(1, 4):
        ret += recur(sum + i)

    dp[sum] = ret % 1000007
    return dp[sum]


n = int(input())
dp = [-1 for i in range(100010)]

answer = recur(0)
print(answer)