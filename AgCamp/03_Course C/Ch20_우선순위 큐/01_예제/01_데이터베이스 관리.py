from heapq import heappush, heappop

n = int(input())
db = []

for i in range(n):
    x = int(input())

    if x == 0:
        if len(db) == 0:
            print(0)
        else:
            print(-heappop(db))
    else:
        heappush(db, -x)  # 큰 값부터 삭제하려면 앞에 - 붙임