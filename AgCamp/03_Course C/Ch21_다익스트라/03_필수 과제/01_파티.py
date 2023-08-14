from heapq import heappush, heappop

INF = int(1e9)


def get_dist(s, v):
    pq = []
    for i in range(1, n + 1):
        visited[i] = False
        dist[i] = INF

    heappush(pq, (0, s))
    dist[s] = 0

    while pq:
        d, cur = heappop(pq)
        if visited[cur]:
            continue

        visited[cur] = True
        for i in v[cur]:
            nxt = i[0]
            nd = d + i[1]
            if dist[nxt] > nd:
                dist[nxt] = nd
                heappush(pq, (nd, nxt))


n, m, k = map(int, input().split())
v = [[] for i in range(1010)]
rv = [[] for i in range(1010)]
visited = [False for i in range(1010)]
dist = [INF for i in range(1010)]
answer = 0

# 1) 정방향, 역방향 그래프 만들기
for i in range(m):
    a, b, c = map(int, input().split())
    v[a].append((b, c))  # 양방향이 아님
    rv[b].append((a, c))

# 2) 시작점에서 다익스트라 1번 실행
get_dist(k, v)
for i in range(1, n + 1):
    answer += dist[i]

get_dist(k, rv)
for i in range(1, n + 1):
    answer += dist[i]

print(answer)