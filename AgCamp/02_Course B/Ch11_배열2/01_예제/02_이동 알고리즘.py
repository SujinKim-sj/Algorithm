n, m, q = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

x, y = 0, 0

for i in range(q):
    d, r = map(int, input().split())

    for i in range(r):
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == -1:
            break
        x = nx
        y = ny

    print(arr[x][y])