from heapq import heappush, heappop

n, m = map(int, input().split())
k = int(input())
pq = []
v = [[] for i in range(20010)]
for i in range(m):
    a, b, c = map(int, input().split())
    v[a].append((b, c))

dist = [0 for i in range(20010)]
for i in range(1, n + 1):
    dist[i] = 2000000000
dist[k] = 0
heappush(pq, (0, k))

while pq:
    mn, cur = heappop(pq)
    if dist[cur] != mn:
        continue
    for j in v[cur]:
        nxt = j[0]
        if dist[nxt] > dist[cur] + j[1]:
            dist[nxt] = dist[cur] + j[1]
            heappush(pq, (dist[nxt], nxt))

for i in range(1, n + 1):
    if dist[i] == 2000000000:
        print("INF")
    else:
        print(dist[i])
