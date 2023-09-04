n = int(input())
dp = [0 for i in range(1000010)]
arr = [0 for i in range(1000010)]
arr2 = list(map(int, input().split()))

for i in range(1, n + 1):
    arr[i] = arr2[i - 1]

answer = 0
for i in range(1, n + 1):
    if dp[i - 1] < dp[i]:
        dp[i] = arr[i]
    else:
        dp[i] = dp[i - 1] + arr[i]
    answer = max(answer, dp[i])

print(answer)