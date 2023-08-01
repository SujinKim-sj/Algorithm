from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
visited = [[False for i in range(1010)] for i in range(1010)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

d = 0
q = deque()
q.append((n - 1, 0))
visited[n - 1][0] = True

while q:
    size = len(q)
    for i in range(size):
        tmp = q.popleft()
        x = tmp[0]
        y = tmp[1]

        if x == 0 and y == m - 1:
            print(d)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 1 or visited[nx][ny]:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True

    d += 1