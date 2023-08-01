from collections import deque

n = int(input())
visited = [False for i in range(100010)]
q = deque()
q.append(1)
visited[1] = True
d = 0

while q:
    size = len(q)
    for i in range(size):
        cur = q.popleft()

        if cur == n:
            print(d)
        if 2 * cur < 100000 and visited[2 * cur] == False:
            q.append(2 * cur)
            visited[2 * cur] = True
        if not visited[cur // 3]:
            q.append(cur // 3)
            visited[cur // 3] = True

    d += 1