# 파이썬에서는 60점이 최대

import sys

n, m = map(int, sys.stdin.readline().split())
prefix = [[0 for i in range(210)] for i in range(210)]
arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i - 1][j - 1]

answer = -10000000

for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(i, n + 1):
            for l in range(j, m + 1):
                sum = prefix[k][l] - prefix[i - 1][l] - prefix[k][j - 1] + prefix[i - 1][j - 1]
                if answer < sum:
                    answer = sum

print(answer)