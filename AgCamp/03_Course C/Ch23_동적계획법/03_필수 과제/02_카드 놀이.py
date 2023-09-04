n = int(input())
arr = [0 for i in range(100010)]
arr2 = list(map(int, input().split()))
dp = [0 for i in range(100010)]

# dp[i] = i번째까지의 카드만 존재할 때 점수의 최댓값
# 바텀업 방식
for i in range(1, n + 1):
    arr[i] = arr2[i - 1]

dp[0] = 0
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i])

print(dp[n])