import sys
from heapq import heappush, heappop

k = int(input())
s = []  # 최소힙
s2 = []  # 최대힙
check = [1] * k

for i in range(k):
    arr = list(map(str, sys.stdin.readline().split()))
    o, n = arr[0], int(arr[1])

    if o == 'I':
        heappush(s, (n, i))
        heappush(s2, (-n, i))
    else:
        if len(s) == 0:
            continue

        if n == 1:  # 최댓값 삭제
            maxv = heappop(s2)[1]
            check[maxv] = 0
        else:  # 최솟값 삭제
            minv = heappop(s)[1]
            check[minv] = 0

        while s and check[s[0][1]] == 0:
            heappop(s)
        while s2 and check[s2[0][1]] == 0:
            heappop(s2)

if len(s) == 0:
    print("EMPTY")
else:
    print(-s2[0][0], s[0][0])