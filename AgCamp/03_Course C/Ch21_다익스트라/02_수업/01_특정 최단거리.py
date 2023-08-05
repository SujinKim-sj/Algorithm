from heapq import heappush, heappop


def get_dist(s):
    pq = []
    for i in range(1, n + 1):
        dist[i] = 1000000000
    dist[s] = 0
    heappush(pq, (0, s))

    while pq:
        d, cur = heappop(pq)
        if dist[cur] != d:
            continue
        for i in v[cur]:
            nxt = i[0]

            if dist[nxt] > dist[cur] + i[1]:
                dist[nxt] = dist[cur] + i[1]
                heappush(pq, (dist[nxt], nxt))


n, m = map(int, input().split())
v = [[] for i in range(1010)]
dist = [0 for i in range(1010)]

for i in range(m):
    a, b, c = map(int, input().split())
    v[a].append((b, c))
    v[b].append((a, c))

a, b = map(int, input().split())
get_dist(a)
a1 = dist[1]
ab = dist[b]
an = dist[n]

get_dist(b)
b1 = dist[1]
ba = dist[a]
bn = dist[n]

print(min(a1 + ab + bn, b1 + ba + an))