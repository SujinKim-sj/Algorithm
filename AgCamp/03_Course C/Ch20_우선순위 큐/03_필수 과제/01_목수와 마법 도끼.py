from heapq import heappush, heappop

# 최대힙

n, h, t = map(int, input().split())
pq = []
count = 0

for i in range(n):
    tree = int(input())
    heappush(pq, -tree)

for i in range(t):
    tmp = -heappop(pq)
    if tmp == 1 or tmp < h:
        break

    tmp //= 2
    heappush(pq, -tmp)
    count += 1

top = -heappop(pq)
if top >= h:
    print("NO")
    print(top)
else:
    print("YES")
    print(count)