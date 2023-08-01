def bfs(x, y):
    global size

    size += 1
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n or arr[nx][ny] == '0' or visited[nx][ny]:
            continue
        bfs(nx, ny)


n = int(input())
arr = [input() for i in range(n)]
visited = [[False for i in range(30)] for i in range(30)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0
answer = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == '0' or visited[i][j]:
            continue
        size = 0
        bfs(i, j)
        answer.append(size)
        cnt += 1

answer.sort()
print(cnt)
for i in range(cnt):
    print(answer[i])