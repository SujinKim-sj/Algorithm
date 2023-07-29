def dfs(x, y):
    global size  # 연결요소의 노드 수

    size += 1
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or maps[nx][ny] == '0' or visited[nx][ny]:
            continue
        dfs(nx, ny)


n = int(input())
visited = [[False for i in range(30)] for i in range(30)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
maps = []

for i in range(n):
    maps.append(input())

cnt = 0  # 단지의 수
answer = []

for i in range(n):
    for j in range(n):
        if maps[i][j] == '0' or visited[i][j]:
            continue
        size = 0
        dfs(i, j)
        answer.append(size)
        cnt += 1

answer.sort()

print(cnt)
for i in range(cnt):
    print(answer[i])